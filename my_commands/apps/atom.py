from dragonfly import Dictation, AppContext, Text, Key, IntegerRef
from breathe import Breathe, CommandContext

context = CommandContext("atom")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = context,
    mapping = {
        '<n> move up': Key('up:%(n)d'),
        '<n> move down': Key('down:%(n)d'),

        'edit undo': Key('c-z'),
        'edit redo': Key('cs-z'),

        '[<n>] edit indent': Key('c-]:%(n)d'),
        '[<n>] edit out dent': Key('c-[:%(n)d'),

        '[<n>] tab right': Key('c-pgdown:%(n)d'),
        '[<n>] tab left': Key('c-pgup:%(n)d'),

        'file save': Key('c-s'),
        'file open': Key('c-o'),

        'edit cut': Key('c-x'),
        'edit copy': Key('c-c'),
        'edit paste': Key('c-v'),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
    ]
)
