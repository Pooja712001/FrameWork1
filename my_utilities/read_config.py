import configparser

config = configparser.RawConfigParser()
config.read("Configuration/config.ini")

class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get("common info", "baseURL")

    @staticmethod
    def get_email():
        return config.get("common info", "email")

    @staticmethod
    def get_password():
        return config.get("common info", "password")
