from dragonfly import Dictation, AppContext, Text, Key
from breathe import Breathe, CommandContext

context = CommandContext("emacs")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = context,
    mapping = {
        'edit undo': Key('cs-_'),

        '[<n>] edit indent': Key('tab:%(n)d'),

        'edit cut': Key('c-w'),
        'edit copy': Key('a-w'),
        'edit paste': Key('c-y'),
    },
    extras = [
    ]
)
