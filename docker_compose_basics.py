# Dockerfile.redis
# docker-compose.yaml
# docker_compose_basics.py


from redis import Redis

cache = Redis(host="redis-hello", port=6379)
cache.incr(name="times", amount=1)
print(cache.get("times"))
