from redis import Redis


class Storage:
    def __init__(self, config):
        self.config = config
        self.redis = Redis(host=self.config.redis_host, port=self.config.redis_port, db=0)
        # при первом запуске приложения "counter" должен быть проинициализирован
        self.counter = f'{self.config.redis_hsetname}counter'
        if not self.redis.hexists(self.counter, "counter"):
            self.redis.hset(self.counter, "counter", 1)

    def add(self, long_link):
        short_link = f'https://do.it/{encode_to_letters(self.redis.hincrby(self.counter, "counter", 1))}'
        return self.redis.hset(self.config.redis_hsetname, short_link, long_link), short_link

    def get(self, short_link):
        return self.redis.hget(self.config.redis_hsetname, short_link)

    def remove(self, short_link):
        return self.redis.hdel(self.config.redis_hsetname, short_link)

    def get_all(self):
        return {k.decode('utf-8'): v.decode('utf-8') for k, v in self.redis.hgetall(self.config.redis_hsetname).items()}


alphabet = [chr(n) for n in range(65, 91)] + [chr(n) for n in range(97, 123)]
alphabet_len = len(alphabet)


def encode_to_letters(number):
    res = ''
    if number >= alphabet_len:
        return res + alphabet[number % alphabet_len] + encode_to_letters(number // alphabet_len)
    else:
        return alphabet[number]
