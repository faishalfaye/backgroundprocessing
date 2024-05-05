from redis import Redis 

r = Redis(host="localhost")
print(r.ping())