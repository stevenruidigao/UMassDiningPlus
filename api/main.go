package main

import (
	// "context"
	"crypto/rand"
	"encoding/hex"
	// "encoding/json"
	// "flag"
	"fmt"
	// "io/ioutil"
	"net/http"
	// "strconv"
	// "strings"
	// "time"

	"github.com/gorilla/mux"
	"github.com/go-redis/redis/v8"
	"github.com/spf13/viper"
)

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
	redisDB := viper.GetString("REDIS_DB")
	cacheToken := viper.GetString("CACHE_TOKEN")
	sessionKey := viper.GetString("SESSION_KEY")
	// cookieMaxAge := viper.GetInt("COOKIE_MAX_AGE")
	writeConfig := viper.GetBool("WRITE_CONFIG")

	if cacheToken == "" {
		bytes := make([]byte, 4)
		rand.Read(bytes)
		cacheToken = hex.EncodeToString(bytes)
	}

	if sessionKey == "" {
		bytes := make([]byte, 32)
		rand.Read(bytes)
		fmt.Println("Empty session key detected: set SESSION_KEY=" + hex.EncodeToString(bytes) + " in .env.")
	}

	if writeConfig {
		viper.WriteConfig()
	}
	
	rdb := redis.NewClient(&redis.Options{
		Addr:     redisHost + ":" + redisPort,
		Password: redisPassword,
		DB:       redisDB,
	})

	router := mux.NewRouter()
	router.PathPrefix("/").Handler(http.FileServer(http.Dir("./public")))
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
