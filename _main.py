import logging
logging.basicConfig()

from my_commands.imports import *

modules = {
    "my_commands": {
        "apps": [
            'emacs',
            'terminal',
            'atom',
            'firefox',
            'chrome',
        ],
        "core": [
            "keys",
            "gnome",
            # "alphanumeric",
        ],
        "languages": ['python', 'latex'],
    }
}

Breathe.load_modules(modules)
