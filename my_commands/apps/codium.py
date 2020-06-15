from dragonfly import Dictation, AppContext, Text, Key, IntegerRef
from breathe import Breathe, CommandContext

context = CommandContext("codium")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = context,
    mapping = {
        'file save': Key('c-s'),
        'file save': Key('c-s'),

        '[<n>] edit indent': Key('c-]:%(n)d'),
        '[<n>] edit out dent': Key('c-[%(n)d'),

        'edit cut': Key('c-x'),
        'edit copy': Key('c-c'),
        'edit paste': Key('c-v'),
        'edit undo': Key('c-z'),

        'toggle problem view': Key('cs-m'),
        'problem next': Key('F8'),

        '[<n>] tab right': Key('c-pgdown:%(n)d'),
        '[<n>] tab left': Key('c-pgup:%(n)d'),

        '[<n>] move tab right': Key('cs-pgdown:%(n)d'),
        '[<n>] move tab left': Key('cs-pgup:%(n)d'),

        'go to line [<NNN>]': Key('c-g') + Text('%(NNN)d\n'),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
        IntegerRef("NNN", 1, 1000, default=1),
    ]
)
