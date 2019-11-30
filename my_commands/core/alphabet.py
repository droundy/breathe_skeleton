from my_commands.imports import *

nato_alphabet = {
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
}

Breathe.add_commands(
    None,
    {
        "[<big>] <letter>": Function(
            lambda big, letter: Text(letter.upper() if big else letter).execute()
        ),
    },
    [
        Choice("big", {"big": True}, default=False),
        Choice("letter", nato_alphabet),
    ]
)
