import redis
import json


class RedisConn:

    def __init__(self):
        self.redis_conn = redis.Redis(host = 'localhost', port = '6379')

    def set(self, key, value, ex = 604800):
        self.redis_conn.set(key, json.dumps(value), ex = ex)

    def get(self, key):
        value = self.redis_conn.get(key)
        try:
            return json.loads(value)
        except Exception as e:
            print('[redis error] ', e)
            return value

    def delete(self, key):
        self.redis_conn.delete(key)

    def incr(self, key):
        self.redis_conn.incr(key)

    def exits(self, key):
        return self.redis_conn.exists(key)


if __name__ == '__main__':
    red = RedisConn()
    # red.set('hello', 'world')
    red.delete('hello')
