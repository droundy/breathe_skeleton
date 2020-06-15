from my_commands.imports import *

Breathe.add_commands(
    context=None,
    mapping={
        "<n> left":          Key("left:%(n)d"),
        "<n> right":         Key("right:%(n)d"),
        "<n> up":            Key("up:%(n)d"),
        "<n> down": Key("down:%(n)d"),

        "<n> lefts":          Key("s-left:%(n)d"),
        "<n> rights":         Key("s-right:%(n)d"),
        "<n> ups":            Key("s-up:%(n)d"),
        "<n> downs": Key("s-down:%(n)d"),

        "[<n>] page down": Key("pgdown:%(n)d"),
        "[<n>] page up": Key("pgup:%(n)d"),
    },
    extras=[
        IntegerRef("n", 1, 20, default=1),
    ]
)

nato_alphabet = {
}

edit_context = CommandContext("editing")

Breathe.add_commands(
    context=edit_context,
    mapping={
        "<n> back space":       Key("backspace:%(n)d"),
        "<n> delete":          Key("delete:%(n)d"),
        "<n> word back space":       Key("c-backspace:%(n)d"),
        "<n> word delete":          Key("c-delete:%(n)d"),
        "<n> space":          Key("space:%(n)d"),
        "end of line":  Key('end'),
        "home of line":  Key('home'),
        "free dictation <text>": Text('%(text)s'),
        "spell <letters>": Function(lambda letters: Text("".join(map(str, letters))).execute()),
    },
    extras=[
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
        Repetition(Choice('letter', {
            'space': ' ',
            'colon': ':',
            'semicolon': ';',
            'period': '.',
            'comma': ',',
            'double quote': '"',
            'single quote': "'",
            'new line': '\n',
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
