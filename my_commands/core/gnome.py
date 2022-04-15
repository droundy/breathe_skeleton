from my_commands.imports import *

import subprocess
import my_commands.apps.firefox as firefox
import my_commands.apps.chrome as chrome
import my_commands.apps.codium as codium
import my_commands.apps.terminal as terminal

import my_commands.core.keys as keys

import my_commands.languages.latex as latex

def enable_context(context):
    context.enable()

def switch_context(context):
    disable_contexts()
    context.enable()

def disable_contexts():
    codium.context.disable()
    firefox.context.disable()
    chrome.context.disable()
    terminal.context.disable()

    latex.context.disable()
    latex.inline_context.disable()

    keys.edit_context.disable()

def notify(*text):
    print(*text)
    subprocess.run(['notify-send', ' '.join(text)])

def start_browsing():
    browse_keys.clear()
    browse_keys.update({
        'left': 'left',
        'right': 'right',
        'up': 'up',
        'down': 'down',
        'select': 'alt:up'
    })
browse_keys = DictList('browse_keys')

Breathe.add_commands(
    context=None,
    mapping={
        "window vee ess code": Key('win/20') + Text('code\n')
                  + Function(lambda: switch_context(codium.context), enable_context(keys.edit_context)),
        "window web": Key('win/20') + Text('web\n'),
        "window zoom": Key('win/20') + Text('zoom\n'),
        "window terminal": Key('win/20') + Text('gnome-terminal\n')
                  + Function(lambda: switch_context(terminal.context), enable_context(keys.edit_context)),
        "window firefox": Key('win/20') + Text('firefox\n'),
        "window chrome": Key('win/20') + Text('chrome\n') + Function(lambda: switch_context(chrome.context)),
        "window journal": Key('win/20') + Text('xournalpp\n'),
        "window settings": Key('win/20') + Text('settings\n'),

        "window change": Key('alt:down')+ Key('tab') + Function(lambda: start_browsing()),
        "window change select": Key('a-tab'),

        "<browse_key>": Key('%(browse_key)s') + Function(lambda browse_key: (browse_keys.clear(), disable_contexts()) if ':' in browse_key else None),

        "window close": Key('c-w'),
        "[<n>] workspace up": Key('ca-up:%(n)d'),
        "[<n>] workspace down": Key('ca-down:%(n)d'),
    },
    extras=[
        IntegerRef("n", 1, 100, default=1),
        DictListRef('browse_key', browse_keys)
    ]
)
