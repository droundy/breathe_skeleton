from dragonfly import Dictation, AppContext, Text, Key
from breathe import Breathe, CommandContext

Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    context = AppContext(title=".py") | CommandContext("python"),
    mapping = {
        "for each"              : Text("for  in :") + Key("left:5"),
        "for loop"              : Text("for i in range():") + Key("left:2"),
        "from import"           : Text("from  import ") + Key("home, right:5"),
        "function"              : Text("def ():") + Key("left:3"),
        "(iffae | iffy)"        : Text("if :") + Key("left"),
        "iffae not"             : Text("if not :") + Key("left"),
        "import"                : Text("import "),
        "lambda"                : Text("lambda :") + Key("left"),
        "while loop"            : Text("while :") + Key("left"),
        "shell iffae"           : Text("elif :") + Key("left"),
        "shells"                : Text("else:"),
        "return"                : Text("return "),
        # ------------------------------------------------
        "method <snaketext>"    : Text("def %(snaketext)s(self):") + Key("left:2"),
        "function [<snaketext>]": Text("def %(snaketext)s():") + Key("left:2"),
        "selfie [<snaketext>]"  : Text("self.%(snaketext)s"),
        "pointer [<snaketext>]" : Text(".%(snaketext)s"),
        "classy [<classtext>]"  : Text("class %(classtext)s:") + Key("left"),
    },
    extras = [
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("classtext", default="").title().replace(" ", ""),
    ]
)
