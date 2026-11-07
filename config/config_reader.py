import json


class ConfigReader:
    _instances = {}
    _DEFAULT_CONFIG_PATH = "config/config.json"

    def __new__(cls, config_path: str = _DEFAULT_CONFIG_PATH):
        if config_path not in cls._instances:
            instance = super().__new__(cls)
            instance._load_config(config_path)
            cls._instances[config_path] = instance
        return cls._instances[config_path]

    def _load_config(self, config_path: str):
        with open(config_path, "r", encoding="utf-8") as f:
            self._config = json.load(f)

    @property
    def base_url(self):
        return self._config["base_url"]

    @property
    def browser(self):
        return self._config["browser"]
