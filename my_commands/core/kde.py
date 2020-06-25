from my_commands.imports import *

import subprocess
import my_commands.apps.firefox as firefox
import my_commands.apps.chrome as chrome
import my_commands.apps.atom as atom
import my_commands.apps.emacs as emacs
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
    emacs.context.disable()
    atom.context.disable()
    terminal.context.disable()

    latex.context.disable()
    latex.inline_context.disable()

    keys.edit_context.disable()

def notify(*text):
    print(*text)
    subprocess.run(['notify-send', ' '.join(text)])

def window_properties():
    notify('executable:', Window.get_foreground().executable)
    notify('title:', Window.get_foreground().title)

def start_browsing():
    browse_keys.clear()
    browse_keys.update({
        'left': 'left',
        'right': 'right',
        # 'up': 'up',
        # 'down': 'down',
        'select': 'escape'
    })
browse_keys = DictList('browse_keys')

Breathe.add_commands(
    context=None,
    mapping={
        # "window emacs": Key('win/20') + Text('emacs\n')
        #           + Function(lambda: switch_context(emacs.context), enable_context(keys.edit_context)),
        # "window atom": Key('win/20') + Text('atom\n')
        #           + Function(lambda: switch_context(atom.context), enable_context(keys.edit_context)),
        # "window codium": Key('win/20') + Text('codium\n')
        #           + Function(lambda: switch_context(codium.context), enable_context(keys.edit_context)),
        # "window web": Key('win/20') + Text('web\n'),
        # "window zoom": Key('win/20') + Text('zoom\n'),
        # "window terminal": Key('win/20') + Text('gnome-terminal\n')
        #           + Function(lambda: switch_context(terminal.context), enable_context(keys.edit_context)),
        # "window firefox": Key('win/20') + Text('firefox\n'),
        # "window chrome": Key('win/20') + Text('chrome\n') + Function(lambda: switch_context(chrome.context)),
        # "window journal": Key('win/20') + Text('xournalpp\n'),
        # "window settings": Key('win/20') + Text('settings\n'),
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
        "workspace south": Key('cs-f8'),
        "workspace southeast": Key('cs-f9'),

        "window switch": Key('a-tab'),
        # "window cycle": Key('alt:down')+ Key('tab') + Function(lambda: start_browsing()),

        "window <direction>": Key('aw-%(direction)s'),

        # "<browse_key>": Key('%(browse_key)s') + Function(lambda browse_key: (browse_keys.clear(), disable_contexts()) if browse_key in ['escape'] else None),

        "window close": Key('c-w'),

        "window properties": Function(window_properties),
    },
    extras=[
        IntegerRef("n", 1, 100, default=1),
        DictListRef('browse_key', browse_keys),
        Choice('direction', {
            'left': 'left',
            'up': 'up',
            'down': 'down',
            'right': 'right',
        }),
    ]
)
