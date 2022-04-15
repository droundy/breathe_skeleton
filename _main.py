from my_commands.imports import Breathe
import logging, os, sys
logging.basicConfig()

#From http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment
desktop = 'unknown'
if sys.platform in ["win32", "cygwin"]:
    desktop = "windows"
elif sys.platform == "darwin":
    desktop = "mac"
else: #Most likely either a POSIX system or something not much common
    desktop_session = os.environ.get("DESKTOP_SESSION")
    print(f"desktop_session is {desktop_session}")
    if 'gnome' in desktop_session:
        desktop = 'gnome'
    elif 'kde' in desktop_session:
        desktop = 'kde'

desktop_fname = f'my_commands/core/{desktop}.py'
if not os.path.exists(desktop_fname):
    print('Desktop {desktop} is unsupported.  Please create {desktop_fname}!')
    exit()

if desktop not in ['gnome', 'kde']:
    print('unsupported desktop: ')

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
            desktop,
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
