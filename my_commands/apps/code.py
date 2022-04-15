from dragonfly import Dictation, AppContext, Text, Key, IntegerRef, Dictation
from breathe import Breathe, CommandContext

context = CommandContext("code")

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context=AppContext('code') | context,
    mapping={
        'file save': Key('c-s'),
        'file open': Key('c-o'),

        '[<n>] edit indent': Key('c-]:%(n)d'),
        '[<n>] edit out dent': Key('c-[:%(n)d'),

        'edit cut': Key('c-x'),
        'edit copy': Key('c-c'),
        'edit paste': Key('c-v'),
        'edit undo': Key('c-z'),

        'edit comment': Key(r'c-slash'),

        'format document': Key('cs-i'),
        'toggle problem view': Key('cs-m'),
        'problem next': Key('F8'),

        '[<n>] tab right': Key('c-pgdown:%(n)d'),
        '[<n>] tab left': Key('c-pgup:%(n)d'),

        '[<n>] move tab right': Key('cs-pgdown:%(n)d'),
        '[<n>] move tab left': Key('cs-pgup:%(n)d'),

        'find <text>': Key('c-f/20') + Text('%(text)s'),
        'match next': Key('enter'),
        'match previous': Key('s-enter'),
        'go to line [<NNN>]': Key('c-g') + Text('%(NNN)d\n'),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
        IntegerRef("NNN", 1, 1000, default=1),
        Dictation("text", default=""),
    ]
)
