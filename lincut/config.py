import os
import re
import yaml


class Config:
    def __init__(self, cfg):
        self._redis_host = cfg['storage']['redis']['host']
        self._redis_port = cfg['storage']['redis']['port']
        self._redis_ttl = cfg['storage']['redis']['ttl']
        self._redis_hsetname = cfg['storage']['redis']['hsetname']

    @property
    def redis_host(self):
        return self._redis_host

    @property
    def redis_port(self):
        return self._redis_port

    @property
    def redis_ttl(self):
        return self._redis_ttl

    @property
    def redis_hsetname(self):
        return self._redis_hsetname


def parse_config(filename):
    pattern = re.compile('^"?\\$\\{([^}^{]+)\\}"?$')

    # можно задавать параметры из переменных окружения, ex. redis_port: ${REDIS_PORT}
    def _path_constructor(loader, node):
        value = node.value
        match = pattern.match(value)
        env_var = match.group().strip('"${}')
        return os.environ.get(env_var) + value[match.end():]

    yaml.add_implicit_resolver('env', pattern, None, yaml.SafeLoader)
    yaml.add_constructor('env', _path_constructor, yaml.SafeLoader)

    with open(filename, "r") as f:
        cfg = yaml.load(f, Loader=yaml.SafeLoader)
    conf = Config(cfg)
    return conf
