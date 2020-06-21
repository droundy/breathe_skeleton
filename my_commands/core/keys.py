from my_commands.imports import *

def modified_directions(n, modifiers0, directions):
    print('got', n, modifiers0, directions)
    for m in modifiers0:
        Key(m+':down').execute()
    for i in range(n):
        for d in directions:
            Key(d).execute()
    for m in modifiers0:
        Key(m+':up').execute()

Breathe.add_commands(
    context=None,
    mapping={
        "[<n>] <modifiers0> <directions> {weight=1e-2}": Function(modified_directions),

        "end of line":  Key('end'),
        "home of line":  Key('home'),

        "[<n>] page down": Key("pgdown:%(n)d"),
        "[<n>] page up": Key("pgup:%(n)d"),
    },
    extras=[
        IntegerRef("n", 1, 20, default=1),
        Repetition(Choice('modifier', {
            'shift': 'shift',
            'control': 'control',
            'alt': 'alt',
        }), name='modifiers', max=3),
        Repetition(Choice('modifier0', {
            'shift': 'shift',
            'control': 'control',
            'alt': 'alt',
        }), name='modifiers0', min=0, max=3),
        Repetition(Choice('direction', {
            'left': 'left',
            'up': 'up',
            'down': 'down',
            'right': 'right',
            'home': 'home',
            'end': 'end',
        }), name='directions', max=10),
    ]
)

edit_context = CommandContext("editing")

Breathe.add_commands(
    context=AppContext('codium') | edit_context,
    mapping={
        "[<n>] back space":       Key("backspace:%(n)d"),
        "[<n>] delete":          Key("delete:%(n)d"),
        "[<n>] word back space":       Key("c-backspace:%(n)d"),
        "[<n>] word delete":          Key("c-delete:%(n)d"),
        # "<n> space":          Key("space:%(n)d"),

        "dictate <text>": Text('%(text)s'),
        "spell <letters>": Function(lambda letters: Text("".join(map(str, letters))).execute()),
    },
    extras=[
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
        Repetition(Choice('letter', {
            'space': ' ',
            'ampersand': '&',
            'colon': ':',
            'equals': '=',
            'minus': '-',
            'semicolon': ';',
            'period': '.',
            'comma': ',',
            'open parenthesis': '(',
            'close parenthesis': ')',
            'double quote': '"',
            'single quote': "'",
            'new line': '\n',
            'zero': '0',
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'niner': '9',
            # NATO alphabet
            "alpha": "a",
            "bravo": "b",
            "charlie": "c",
            "delta": "d",
            "echo": "e",
            "foxtrot": "f",
            "golf": "g",
            "hotel": "h",
            "india": "i",
            "juliet": "j",
            "kilo": "k",
            "lima": "l",
            "mike": "m",
            "november": "n",
            "oscar": "o",
            "papa": "p",
            "quebec": "q",
            "romeo": "r",
            "sierra": "s",
            "tango": "t",
            "uniform": "u",
            "victor": "v",
            "whiskey": "w",
            "x-ray": "x",
            "yankee": "y",
            "zulu": "z",

            "big alpha": "A",
            "big bravo": "B",
            "big charlie": "C",
            "big delta": "D",
            "big echo": "E",
            "big foxtrot": "F",
            "big golf": "G",
            "big hotel": "H",
            "big india": "I",
            "big juliet": "J",
            "big kilo": "K",
            "big lima": "L",
            "big mike": "M",
            "big november": "N",
            "big oscar": "O",
            "big papa": "P",
            "big quebec": "Q",
            "big romeo": "R",
            "big sierra": "S",
            "big tango": "T",
            "big uniform": "U",
            "big victor": "V",
            "big whiskey": "W",
            "big x-ray": "X",
            "big yankee": "Y",
            "big zulu": "Z",
        }), name='letters'),
    ]
)
