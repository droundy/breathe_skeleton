from my_commands.imports import Breathe
import logging
logging.basicConfig()


modules = {
    "my_commands": {
        "apps": [
            'code',
            'terminal',
            'firefox',
            'chrome',
            'gmail',
        ],
        "core": [
            "keys",
            # "kde",
            "gnome",
            # "alphanumeric",
        ],
        "languages": [
            'rust',
            'python',
            'latex',
        ],
    }
}

Breathe.load_modules(modules)
