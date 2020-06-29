from dragonfly import AppContext, Dictation, Text, Key, IntegerRef
from breathe import Breathe, CommandContext

context = CommandContext("chrome")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = AppContext('chrome') | context,
    mapping = {
        'page back': Key('a-left'),
        'page forward': Key('a-right'),
        'page reload': Key('cs-r'),

        'search for <text>': Key('a-d/20') + Text('%(text)s\n'),

        'tab new': Key('c-t'),
        'tab close': Key('c-w'),

        '[<n>] link next': Key('tab:%(n)d'),
        '[<n>] link previous': Key('s-tab:%(n)d'),
        'link follow': Key('enter'),

        '[<n>] tab right': Key('c-pgdown:%(n)d'),
        '[<n>] tab left': Key('c-pgup:%(n)d'),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)
