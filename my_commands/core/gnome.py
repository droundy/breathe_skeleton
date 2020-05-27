from my_commands.imports import *

Breathe.add_commands(
    context=None,
    mapping={
        "window emacs": Key('win/20') + Text('emacs\n'),
        "window atom": Key('win/20') + Text('atom\n'),
        "window terminal": Key('win/20') + Text('gnome-terminal\n'),
        "window firefox": Key('win/20') + Text('firefox\n'),
        "window chrome": Key('win/20') + Text('chrome\n'),
        "window journal": Key('win/20') + Text('xournalpp\n'),
        "window settings": Key('win/20') + Text('settings\n'),
        "window close": Key('c-w'),
        "[<n>] workspace up": Key('ca-up:%(n)d'),
        "[<n>] workspace down": Key('ca-down:%(n)d'),
    },
    extras=[
        IntegerRef("n", 1, 100, default=1),
    ]
)
