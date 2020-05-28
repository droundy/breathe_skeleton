import logging
logging.basicConfig()

from my_commands.imports import *

modules = {
    "my_commands": {
        "apps": [],
        "core": [
            "keys",
            "gnome",
            # "alphanumeric",
        ],
        "languages": ['python', 'latex'],
    }
}

Breathe.load_modules(modules)
