from my_commands.imports import *

import subprocess
import my_commands.apps.firefox as firefox
import my_commands.apps.chrome as chrome
import my_commands.apps.atom as atom
import my_commands.apps.emacs as emacs
import my_commands.apps.terminal as terminal

import my_commands.core.keys as keys

import my_commands.languages.latex as latex

def enable_context(context):
    context.enable()

def switch_context(context):
    disable_contexts()
    context.enable()

def disable_contexts():
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

Breathe.add_commands(
    context=None,
    mapping={
        "window emacs": Key('win/20') + Text('emacs\n')
                  + Function(lambda: switch_context(emacs.context), enable_context(keys.edit_context)),
        "window atom": Key('win/20') + Text('atom\n')
                  + Function(lambda: switch_context(atom.context), enable_context(keys.edit_context)),
        "window web": Key('win/20') + Text('web\n'),
        "window zoom": Key('win/20') + Text('zoom\n'),
        "window terminal": Key('win/20') + Text('gnome-terminal\n')
                  + Function(lambda: switch_context(terminal.context), enable_context(keys.edit_context)),
        "window firefox": Key('win/20') + Text('firefox\n'),
        "window chrome": Key('win/20') + Text('chrome\n') + Function(lambda: switch_context(chrome.context)),
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
