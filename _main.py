import logging
logging.basicConfig()

from my_commands.imports import Breathe

modules = {
    "my_commands": {
        "apps": [
            'emacs',
            'codium',
            'terminal',
            'atom',
            'firefox',
            'chrome',
            'gmail',
            'gradescope',
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
