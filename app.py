import time
from config import create_app, create_cache
import os
import redis
from flask import Flask

app = Flask(__name__)

HOST = "redis-testing" if os.getenv("TEST", None) else "redis"
cache = redis.Redis(host=HOST, port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route("/")
def hello():
    count = get_hit_count()
    return "Hello World! I have been seen {} times.\n".format(count)
