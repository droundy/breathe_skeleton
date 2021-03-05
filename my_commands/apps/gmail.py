from dragonfly import Dictation, AppContext, Text, Key, IntegerRef, Choice, Repetition, Function
from breathe import Breathe, CommandContext

context = CommandContext("gmail")

def do_commands(commands):
    for c in commands:
        Key(c).execute()

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = AppContext(title='Gmail') | AppContext(title='Mail -') | context,
    mapping = {
        'message <commands>': Function(do_commands),
        '[<n>] message next': Key('j:%(n)d'),
        '[<n>] message previous': Key('k:%(n)d'),
    },
    extras = [
        Repetition(Choice('message', {
            'select': 'x',
            'next': 'j',
            'previous': 'k',
            'archive': 'e',
            'delete': '#',
            'reply': 'r',
            'reply all': 'a',
            'send': 'c-enter',
            'view': 'enter',
            'compose': 'c',
        }), name='commands', max=20),
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)
