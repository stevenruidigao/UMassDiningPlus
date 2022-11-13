package main

import (
	"context"
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"log"

	// "encoding/json"
	// "flag"
	"fmt"
	// "io/ioutil"
	"net/http"
	// "strconv"
	"strings"
	"time"

	"github.com/go-redis/redis/v8"
	"github.com/gorilla/mux"
	"github.com/igm/pubsub"
	"github.com/igm/sockjs-go/v3/sockjs"
	"github.com/spf13/viper"
)

type Details struct {
	Location     string    `json:"location"`
	LocationName string    `json:"locationName"`
	Address      string    `json:"address"`
	Loads        []float64 `json:"loads"`
	Time         time.Time `json:"time"`
	Success      bool      `json:"success"`
	Message      string    `json:"message"`
}

var ctx = context.Background()
var publisher pubsub.Publisher
var redisClient *redis.Client

func main() {
	viper.SetConfigFile(".env")
	viper.AutomaticEnv()
	viper.SetDefault("ENV", "development")
	viper.SetDefault("HOST", "")
	viper.SetDefault("PORT", "8080")
	viper.SetDefault("REDIS_HOST", "")
	viper.SetDefault("REDIS_PASSWORD", "")
	viper.SetDefault("REDIS_PORT", "6379")
	viper.SetDefault("REDIS_DB", 0)
	viper.SetDefault("COOKIE_MAX_AGE", 86400*30)
	err := viper.ReadInConfig()

	if err != nil {
		panic("Error reading config .env")
	}

	// env := viper.GetString("ENV")
	host := viper.GetString("HOST")
	port := viper.GetString("PORT")
	redisHost := viper.GetString("REDIS_HOST")
	redisPort := viper.GetString("REDIS_PORT")
	redisPassword := viper.GetString("REDIS_PASSWORD")
	redisDB := viper.GetInt("REDIS_DB")
	cacheToken := viper.GetString("CACHE_TOKEN")
	sessionKey := viper.GetString("SESSION_KEY")
	// cookieMaxAge := viper.GetInt("COOKIE_MAX_AGE")
	writeConfig := viper.GetBool("WRITE_CONFIG")

	if cacheToken == "" {
		bytes := make([]byte, 4)
		rand.Read(bytes)
		// cacheToken = hex.EncodeToString(bytes)
	}

	if sessionKey == "" {
		bytes := make([]byte, 32)
		rand.Read(bytes)
		fmt.Println("Empty session key detected: set SESSION_KEY=" + hex.EncodeToString(bytes) + " in .env.")
	}

	if writeConfig {
		viper.WriteConfig()
	}

	redisClient = redis.NewClient(&redis.Options{
		Addr:     redisHost + ":" + redisPort,
		Password: redisPassword,
		DB:       redisDB,
	})

	router := mux.NewRouter()
	apiRouter := router.PathPrefix("/api").Subrouter()
	v1Router := apiRouter.PathPrefix("/v1").Subrouter()

	v1Router.HandleFunc("/details/{location}", func(writer http.ResponseWriter, request *http.Request) {
		location := mux.Vars(request)["location"]
		fmt.Println("Get details of", location)
		details := []Details{{Location: location, Message: "Success.", Success: true, Time: time.Now()}}
		details[0].Loads, err = getLocationLoads(location)

		if err != nil {
			if err == redis.Nil {
				details[0].Message = "That location does not exist."

			} else {
				details[0].Message = "An unknown error occurred: " + err.Error()
			}

			details[0].Success = false
			json.NewEncoder(writer).Encode(details)
			return
		}

		locationName, err := getLocationName(location)

		if err != nil {
			if err == redis.Nil {
				details[0].Message = "That location does not exist."

			} else {
				details[0].Message = "An unknown error occurred: " + err.Error()
			}

			details[0].Success = false
			json.NewEncoder(writer).Encode(details)
			return
		}

		details[0].LocationName = locationName
		json.NewEncoder(writer).Encode(details)
	})

	v1Router.HandleFunc("/locations", func(writer http.ResponseWriter, request *http.Request) {
		locations, err := redisClient.SMembers(ctx, "umadp:locations").Result()
		fmt.Println("Get locations")

		if err != nil {
			fmt.Println("An error occurred while getting the list of available locations:", err)
		}

		json.NewEncoder(writer).Encode(locations)
	})

	v1Router.PathPrefix("/socket/").Handler(sockjs.NewHandler("/api/v1/socket", sockjs.DefaultOptions, connectionHandler))
	Update()

	router.PathPrefix("/").Handler(http.FileServer(http.Dir("./public")))
	router.PathPrefix("/").Handler(http.FileServer(http.Dir("./public/client")))
	router.PathPrefix("/").Handler(http.FileServer(http.Dir("./public/prerendered")))
	router.PathPrefix("/").Handler(http.FileServer(http.Dir("./public/server")))
	fmt.Println("Listening on " + host + ":" + port)
	http.ListenAndServe(host+":"+port, router)

	/*
			    err := rdb.Set(ctx, "key", "value", 0).Err()
		    if err != nil {
		        panic(err)
		    }

		    val, err := rdb.Get(ctx, "key").Result()
		    if err != nil {
		        panic(err)
		    }
		    fmt.Println("key", val)

		    val2, err := rdb.Get(ctx, "key2").Result()
		    if err == redis.Nil {
		        fmt.Println("key2 does not exist")
		    } else if err != nil {
		        panic(err)
		    } else {
		        fmt.Println("key2", val2)
		    }
	*/
}

func getLocationLoads(location string) ([]float64, error) {
	loads := []float64{}
	loadString, err := redisClient.Get(ctx, "umadp:location:"+location+":loads").Result()

	if err != nil {
		return loads, err
	}

	fmt.Println("loads:", loadString)
	err = json.Unmarshal([]byte(loadString), &loads)

	if err != nil {
		return loads, err
	}

	return loads, nil
}

func getLocationName(location string) (string, error) {
	return redisClient.Get(ctx, "umadp:location:"+location+":name").Result()
}

func getLocationsDetails() []Details {
	locations, err := redisClient.SMembers(ctx, "umadp:locations").Result()

	if err != nil {
		fmt.Println("An error occurred while getting the list of available locations:", err)
		return []Details{}
	}

	details := make([]Details, len(locations))

	for i, location := range locations {
		details[i] = Details{Location: location, Message: "Success.", Success: true, Time: time.Now()}
		details[i].Loads, err = getLocationLoads(location)

		if err != nil {
			details[i].Message = "An error occurred:" + err.Error()
			details[i].Success = false
			fmt.Println("An error occurred:", err)
			continue
		}

		details[i].LocationName, err = getLocationName(location)

		if err != nil {
			details[i].Message = "An error occurred:" + err.Error()
			details[i].Success = false
			fmt.Println("An error occurred:", err)
			continue
		}
	}

	return details
}

func Update() {
	rawUpdate, _ := json.Marshal(getLocationsDetails())
	publisher.Publish(string(rawUpdate))
	time.AfterFunc(30*time.Second, Update)
}

func connectionHandler(session sockjs.Session) {
	fmt.Println("New SockJS session established.")
	closedSession := make(chan struct{})
	rawUpdate, _ := json.Marshal(getLocationsDetails())

	session.Send(string(rawUpdate))
	// if err := session.Send(string(rawUpdate)); err != nil {
	// 	return
	// }

	// publisher.Publish("[info] new participant joined chat")
	// defer publisher.Publish("[info] participant left chat")
	go func() {
		reader, _ := publisher.SubChannel(nil)

		for {
			select {
			case <-closedSession:
				return

			case msg := <-reader:
				if err := session.Send(msg.(string)); err != nil {
					return
				}
			}
		}
	}()

	for {
		if msg, err := session.Recv(); err == nil {
			details := []Details{{Message: "Success.", Success: true, Time: time.Now()}}

			if strings.Contains(msg, "umadp:location: ") {
				messageParts := strings.Split(msg, "umadp:location: ")

				if len(messageParts) < 2 {
					details[0].Message = "Malformed request."
					details[0].Success = false
					rawResponse, _ := json.Marshal(details)

					if err := session.Send(string(rawResponse)); err != nil {
						break
					}
				}

				location := strings.Split(msg, "umadp:location: ")[1]
				details[0].Location = location

				if err != nil {
					if err == redis.Nil {
						details[0].Message = "That location does not exist."

					} else {
						details[0].Message = "An unknown error occurred: " + err.Error()
					}

					details[0].Success = false
					rawResponse, _ := json.Marshal(details)

					if err := session.Send(string(rawResponse)); err != nil {
						break
					}

					return
				}

				locationName, err := getLocationName(location)

				if err != nil {
					if err == redis.Nil {
						details[0].Message = "That location does not exist."

					} else {
						details[0].Message = "An unknown error occurred: " + err.Error()
					}

					details[0].Success = false
					rawResponse, _ := json.Marshal(details)

					if err := session.Send(string(rawResponse)); err != nil {
						break
					}

					return
				}

				details[0].LocationName = locationName
				rawResponse, _ := json.Marshal(details)

				if err := session.Send(string(rawResponse)); err != nil {
					break
				}
			}
			continue
		}
		break
	}

	close(closedSession)
	log.Println("SockJS session closed.")
}
