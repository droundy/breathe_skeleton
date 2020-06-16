from dragonfly import Dictation, AppContext, Text, Key, IntegerRef
from breathe import Breathe, CommandContext

context = CommandContext("gmail")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = context,
    mapping = {
        'message select': Key('x'),
        'message archive': Key('e'),
        'message delete': Key('#'),
        'message reply': Key('r'),
        'message reply all': Key('a'),
        'message send': Key('c-enter'),
        '[<n>] message next': Key('j:%(n)d'),
        '[<n>] message previous': Key('k:%(n)d'),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)
