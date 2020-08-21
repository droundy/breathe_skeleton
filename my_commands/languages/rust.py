from dragonfly import Dictation, AppContext, Text
from breathe import Breathe, CommandContext

context = CommandContext("rust")

keywords = [
    'self',
    # 'for', 'in',
    # 'if', 'else',
    # 'import', 'from', 'def', 'class', 'pass', 'return',
]

mapping = {
    'open curly': Text('{'),
    'open parenthesis': Text('('),
    'open square': Text('['),
    'dot': Text('.'),
    'colon': Text(':\n'),
    'you size': Text('usize'),
    'you sixty four': Text('u64 '),
    'f sixty four': Text('f64 '),
    'define function': Text('fn '),
    'ice sixty four': Text('i64 '),
    'boolean': Text('bool '),
    'struct': Text('struct '),
    'function': Text('fn '),
    'e numb': Text('enum '),
    'it er': Text('iter()'),
    'imple': Text('impl '),
    'function returns': Text(' -> '),
    'match gives': Text(' => '),
    'start match': Text('match '),
    'let': Text('let '),
    'mute': Text('mut '),
    'pub': Text('pub '),
    "snake case [<snaketext>]" : Text("%(snaketext)s"),
    "screaming snake case [<screamingsnaketext>]" : Text("%(screamingsnaketext)s"),
    "camel case [<CamelText>]"  : Text("%(CamelText)s"),
}
for k in keywords:
    mapping[k] = Text(k + ' ')

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = AppContext(title='.rs') | context,
    mapping = mapping,
    extras = [
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("screamingsnaketext", default="").upper().replace(" ", "_"),
        Dictation("CamelText", default="").title().replace(" ", ""),
    ]
)
