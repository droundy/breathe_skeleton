import logging
logging.basicConfig()

from my_commands.imports import *

modules = {
    "my_commands": {
        "apps": [],
        "core": [
            "keys",
            "alphabet",
        ],
        "languages": [],
    }
}

Breathe.load_modules(modules)