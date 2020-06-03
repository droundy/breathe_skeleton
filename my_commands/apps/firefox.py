from dragonfly import Dictation, AppContext, Text, Key
from breathe import Breathe, CommandContext

context = CommandContext("firefox")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = context,
    mapping = {
        'page back': Key('a-left'),
        'page forward': Key('a-right'),
    },
    extras = [
    ]
)
