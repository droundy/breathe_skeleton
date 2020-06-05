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
        IntegerRef("n", 1, 100, default=1),
    ]
)

edit_context = CommandContext("editing")

Breathe.add_commands(
    context=edit_context,
    mapping={
        "<n> back space":       Key("backspace:%(n)d"),
        "<n> delete":          Key("delete:%(n)d"),
        "<n> space":          Key("space:%(n)d"),
        "dictate <text>": Text('%(text)s'),
    },
    extras=[
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)

spelling_context = CommandContext("spelling")

Breathe.add_commands(
    context=spelling_context,
    mapping={
        "a":       Key("a"),
        "b":       Key("b"),
        "c":       Key("c"),
        "d":       Key("d"),
        "e":       Key("e"),
        "f":       Key("f"),
        "g":       Key("g"),
        "h":       Key("h"),
        "i":       Key("i"),
        "j":       Key("j"),
        "k":       Key("k"),
        "l":       Key("l"),
        "m":       Key("m"),
        "n":       Key("n"),
        "o":       Key("o"),
        "p":       Key("p"),
        "q":       Key("q"),
        "r":       Key("r"),
        "s":       Key("s"),
        "t":       Key("t"),
        "u":       Key("u"),
        "v":       Key("v"),
        "w":       Key("w"),
        "x":       Key("x"),
        "y":       Key("y"),
        "z":       Key("z"),
    },
    extras=[
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)
