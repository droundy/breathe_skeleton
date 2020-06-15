from dragonfly import Dictation, AppContext, Text, Key, IntegerRef, Choice
from breathe import Breathe, CommandContext

context = CommandContext("grade scope")

querty_alphabet = {
    "q": "q",
    "w": "w",
    "e": "e",
    "r": "r",
    "t": "t",
    "y": "y",
    "u": "u",
    "i": "i",
}

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = context,
    mapping = {
        'grade <n>': Key('%(n)d'),
        'grade <n> correct': Text('%(n)dq'),
        'grade <n> wrong': Text('%(n)dw'),
        'grade <qwerty>': Key('%(qwerty)s'),
        'problem next': Key('.'),
        'problem previous': Key(','),
        'next page': Key('k'),
        'previous page': Key('j'),
        'next ungraded': Key('z'),
        'next exam': Key('right'),
        'previous exam': Key('left'),
    },
    extras = [
        IntegerRef("n", 1, 10, default=1),
        Dictation("text", default=""),
        Choice('qwerty', querty_alphabet),
    ]
)
