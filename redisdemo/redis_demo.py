# coding=utf-8

from redis import Redis


class RedisF(object):
    def __init__(self):
        self.host = '192.168.89.129'
        self.port = 6379
        self.password = '123456'

        self.redis_obj = Redis(host=self.host, port=self.port, password=self.password,
                               decode_responses=True, charset='utf-8', encoding='utf-8')

    def set_mset(self, input_dict):
        self.redis_obj.mset(input_dict)

    def get_mget(self, key_list):
        return self.redis_obj.mget(key_list)


if __name__ == "__main__":
    s_dict = {"name": "xjzhao", "age": 30, "company": "志翔科技"}
    s_list = ["name", "age", "company"]

    r = RedisF()
    result = r.get_mget(s_list)
    print(result)
