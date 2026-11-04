import json
import os


class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            config_path = os.path.join(os.path.dirname(__file__), "config.json")
            with open(config_path, "r", encoding="utf-8") as f:
                cls._instance.config = json.load(f)
        return cls._instance

    @property
    def base_url(self):
        return self.config["base_url"]

    @property
    def browser(self):
        return self.config["browser"]
#этот код полностью написан дипсиком. сам бы я не додумался написать его, для меня сложно