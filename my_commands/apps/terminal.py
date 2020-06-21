from dragonfly import Dictation, AppContext, Text, Key, IntegerRef, Function
from breathe import Breathe, CommandContext
import subprocess

context = CommandContext("terminal")

def notify(*text):
    print(*text)
    subprocess.run(['notify-send', ' '.join(text)])

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = AppContext(executable='terminal') | context,
    mapping = {
        'window new': Key('cs-n'),

        'git diff': Text('git diff\n'),
        'git status': Text('git status\n'),
        'git commit minus a m <text>': Text('git commit -am "%(text)s"\n'),
        'git commit minus m <text>': Text('git commit -m "%(text)s"\n'),
        'git <text>': Function(lambda text: notify('unrecognized git command:', str(text))),
        'codium here': Text('codium -n --folder-uri `pwd` &\n'),

        'control c': Key('c-c'),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)
