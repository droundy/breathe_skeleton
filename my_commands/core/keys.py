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
