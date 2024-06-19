import unittest
import redis

from app import app
from config import create_cache


class TestRedis(unittest.TestCase):
    def setUp(self):
        self.redis_server = create_cache("redis-testing", 6379)

    def test_redis_connection(self):
        try:
            self.redis_server.ping()
        except redis.ConnectionError:
            self.fail("Could not connect to Redis server")

    def test_redis_set_get(self):
        try:
            self.redis_server.set("test_key", "test_value")
            value = self.redis_server.get("test_key")
            self.assertEqual(value.decode("utf-8"), "test_value")
        except redis.RedisError:
            self.fail("Redis operation failed")


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get("/")
        self.assertEqual(response.data, b"Hello World! I have been seen 1 times.\n")
