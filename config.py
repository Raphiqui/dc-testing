from flask import Flask
import redis


def create_cache(redis_host, redis_port):
    return redis.Redis(host=redis_host, port=redis_port)


def create_app():
    app = Flask(__name__)
    return app
