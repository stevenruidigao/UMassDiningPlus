import json
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def updateLoads(location, load):
   loads = json.loads(redis_client.get('dp:location:' + location + ':loads'))
   loads.push(load)
   redis_client.set('dp:location:' + location + ':loads', json.dumps(loads))