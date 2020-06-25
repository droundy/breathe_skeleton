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
            "kde",
            # "gnome",
            # "alphanumeric",
        ],
        "languages": ['rust', 'python', 'latex'],
    }
}

Breathe.load_modules(modules)
