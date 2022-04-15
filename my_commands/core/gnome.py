from my_commands.imports import *

Breathe.add_commands(
    context=None,
    mapping={
        # "window terminal": Key('a-f2/20') + Text('gnome-terminal') + Key('enter'),
        # "window chrome": Key('a-f2/20') + Text('google-chrome') + Key('enter'),
        # "window journal": Key('a-f2/20') + Text('xournalpp') + Key('enter'),
        "window full screen": Key('w-up'),
        "window full <direction>": Key('w-%(direction)s'),
        # "window full right": Key('w-right'),
        # "window full up": Key('w-up'),
        # "window full down": Key('w-down'),

        "workspace switch": Key('w-tab'),
        "workspace up": Key('ca-up'),
        "workspace down": Key('ca-down'),

        "window switch": Key('a-tab'),

        # The following doesn't work under Gnome.
        # "window <direction>": Key('aw-%(direction)s'),

        # "<browse_key>": Key('%(browse_key)s') + Function(lambda browse_key: (browse_keys.clear(), disable_contexts()) if browse_key in ['escape'] else None),

        "window close": Key('c-w'),
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
