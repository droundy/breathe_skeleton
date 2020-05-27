from dragonfly import Dictation, AppContext, Text, Key
from breathe import Breathe, CommandContext

keywords = [
    'for', 'in',
    'if', 'else',
    'import', 'from', 'def', 'class', 'pass', 'return',
]
functions = ['range', 'print']

mapping = {
    'colon': Text(':\n'),
    'comma': Text(', '),
    '(ell if|else if)': Text('elif '),
    "snake case [<snaketext>]" : Text("%(snaketext)s"),
    "screaming snake case [<screamingsnaketext>]" : Text("%(screamingsnaketext)s"),
    "Camel Case [<CamelText>]"  : Text("%(CamelText)s"),
}
for k in keywords:
    mapping[k] = Text(k + ' ');
for k in functions:
    mapping[k] = Text(k + '()') + Key('left');

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    context = AppContext(title=".py") | CommandContext("python"),
    mapping = mapping,
    extras = [
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("screamingsnaketext", default="").upper().replace(" ", "_"),
        Dictation("CamelText", default="").title().replace(" ", ""),
    ]
)
