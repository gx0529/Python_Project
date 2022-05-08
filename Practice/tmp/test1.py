

import configparser
import os
config = configparser.ConfigParser()

config.read("./config.ini")

timer = config.get("mingling", "value")

print(timer)

os.system(timer)
