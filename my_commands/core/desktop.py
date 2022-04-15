from my_commands.imports import *

# From http://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment
desktop = 'unknown'
if sys.platform in ["win32", "cygwin"]:
    desktop = "windows"
elif sys.platform == "darwin":
    desktop = "mac"
else:  # Most likely either a POSIX system or something not much common
    desktop_session = os.environ.get("DESKTOP_SESSION")
    print(f"desktop_session is {desktop_session}")
    if 'gnome' in desktop_session:
        desktop = 'gnome'
    elif 'kde' in desktop_session:
        desktop = 'kde'


# Handling multiple desktops

# The code below introduces bindings for multiple different desktops.  A given
# binding is silently ignored if an action is not defined for the desktop we are
# running on.  That seems better than doing something random.

Breathe.add_commands(
    context=None,
    mapping={
        k: bindings[desktop] for k, bindings in
        {
            # "window terminal": Key('a-f2/20') + Text('gnome-terminal') + Key('enter'),
            # "window chrome": Key('a-f2/20') + Text('google-chrome') + Key('enter'),
            # "window journal": Key('a-f2/20') + Text('xournalpp') + Key('enter'),
            "window full screen": {
                'gnome': Key('w-up'),
                'kde': Key('w-up'),
            },
            "window full <direction>": {
                'gnome': Key('w-%(direction)s'),
                'kde': Key('w-%(direction)s'),
            },

            # "workspace switch": Key('w-tab'),
            "workspace up": {
                'gnome': Key('ca-up'),
                'kde': Key('cw-up'),
            },
            "workspace down": {
                'gnome': Key('ca-down'),
                'kde': Key('cw-down'),
            },

            "window switch": {
                'gnome': Key('a-tab'),
                'kde': Key('w-tab'),
            },

            "window <direction>": {
                'kde': Key('aw-%(direction)s'),
            },

            # "<browse_key>": Key('%(browse_key)s') + Function(lambda browse_key: (browse_keys.clear(), disable_contexts()) if browse_key in ['escape'] else None),

            "window close": {
                'gnome': Key('c-w'),
                'kde': Key('c-w'),
            },
        }.items()
        if desktop in bindings
    },
    extras=[
        # IntegerRef("n", 1, 100, default=1),
        # DictListRef('browse_key', browse_keys),
        Choice('direction', {
            'left': 'left',
            'up': 'up',
            'down': 'down',
            'right': 'right',
        }),
    ]
)
