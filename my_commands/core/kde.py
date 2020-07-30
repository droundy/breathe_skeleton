from my_commands.imports import *

import subprocess

def notify(*text):
    print(*text)
    subprocess.run(['notify-send', ' '.join(text)])

def window_properties():
    notify('executable:', Window.get_foreground().executable)
    notify('title:', Window.get_foreground().title)

# def start_browsing():
#     browse_keys.clear()
#     browse_keys.update({
#         'left': 'left',
#         'right': 'right',
#         # 'up': 'up',
#         # 'down': 'down',
#         'select': 'escape'
#     })
# browse_keys = DictList('browse_keys')

Breathe.add_commands(
    context=None,
    mapping={
        "window terminal": Key('a-f2/20') + Text('gnome-terminal') + Key('enter'),
        "window chrome": Key('a-f2/20') + Text('google-chrome') + Key('enter'),
        "window journal": Key('a-f2/20') + Text('xournalpp') + Key('enter'),

        "workspace grid": Key('c-f8')+ Function(lambda: start_browsing()),
        "workspace gmail": Key('alt:up') + Key('c-f1'),
        "workspace computational lab": Key('c-f2'),
        "workspace class": Key('c-f3'),
        "workspace dragonfly": Key('c-f4'),
        "workspace monte carlo": Key('cs-f5'),
        "workspace paper": Key('cs-f6'),
        "workspace dynein": Key('cs-f7'),
        "workspace website": Key('cs-f8'),
        "workspace fun": Key('cs-f9'),
        "workspace extra": Key('cs-f10'),

        "window switch": Key('a-tab'),
        # "window cycle": Key('alt:down')+ Key('tab') + Function(lambda: start_browsing()),

        "window <direction>": Key('aw-%(direction)s'),

        # "<browse_key>": Key('%(browse_key)s') + Function(lambda browse_key: (browse_keys.clear(), disable_contexts()) if browse_key in ['escape'] else None),

        "window close": Key('c-w'),

        "window properties": Function(window_properties),
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
