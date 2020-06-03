from dragonfly import Dictation, AppContext, Text, Key, \
     Function, Choice, Integer
from breathe import Breathe, CommandContext, Exec, CommandsRef

def start_inline():
    context.disable()
    inline_context.enable()
def end_math():
    inline_context.disable()
    context.enable()

context = CommandContext("latex")
inline_context = CommandContext("inline math")
Breathe.add_commands(
    context = context,
    mapping = {
        'dictate <latex>': Text('%(latex)s\n'),
        'emphasize <latex>': Text(r'\emph{}%(latex)s}\n'),
        'inline math': Text('$')+Function(start_inline),
        # 'align math': Text('$')+Function(go_align),
    },
    extras = [
        Dictation("latex", default="").lower().replace(" new paragraph ", "\n\n"),
    ]
)

functions = {
   'square root': r'\sqrt',
   'sine': r'\sin',
   'cosine': r'\cos',
   'tangent': r'\tan',
   'exponential': r'\exp',
}
# fraction sin x ^2squared divided by 3 + x
#  \frac{\sin(x^2)}{3+x}
Breathe.add_commands(
    context = inline_context,
    mapping = {
      "<expr1> frac <expr2> over <expr3>":
          Exec("expr1") + Text("\\frac{") + Exec("expr2") + Text("}{") + Exec("expr3") + Text("}"),
      "<expr1> over <expr2>":
          Text("\\frac{") + Exec("expr1") + Text("}{") + Exec("expr2") + Text("}"),
      "<expr1> of <expr2>":
          Exec("expr1") + Text("\\left(") + Exec("expr2") + Text("\\right)"),
      "<expr1> e to the <expr2>":
          Exec("expr1") + Text(" e^{") + Exec("expr2") + Text("}"),
    },
    extras = [
        CommandsRef("expr1", 8),
        CommandsRef("expr2", 8),
        CommandsRef("expr3", 8),
    ],
    top_level=True,
)
variable = Choice("variable", {
        "psi": r"\psi",
        "phi": r"\phi",
        "big psi": r"\Psi",
        "pi": r"\pi",
        "i": r" i",
        "j": r" j",
        "k": r" k",
        "x": r" x",
        "y": r" y",
        "z": r" z",
    })
nth = Choice("nth", {
        "first": "1",
        "second": "2",
        "third": "3",
        "fourth": "4",
        "fifth": "5",
        "sixth": "6",
        "seventh": "7",
        "eighth": "8",
        "nineth": "9",
    })
# variables = {
#     'psi': r'\psi',
#     'phi': r'\phi',
#     'pi': r'\pi',
#     'i': r'i',
# }
math_mapping = {}
# for v, t in variables:
#     math_mapping[v] = Text(t)

inline_mapping = {
    'done': Text('$ ')+Function(start_inline),
    '<variable>': Text('%(variable)s'),
    'squared': Text('^2'),
    'plus': Text('+'),
    'minus': Text('-'),
    '(times|cross)': Text(r'\times'),
    'dot': Text(r'\dot'),
    'to the <nth>': Text('^%(nth)s'),
    '<n>': Text('%(n)d'),
}
for k,v in math_mapping:
    inline_mapping[k] = v
for k,v in functions.items():
    inline_mapping[k] = Text(v)
Breathe.add_commands(
    context = inline_context,
    mapping = inline_mapping,
    extras = [
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("screamingsnaketext", default="").upper().replace(" ", "_"),
        Dictation("CamelText", default="").title().replace(" ", ""),
        variable,
        nth,
        Integer('n', 0, 300),
    ]
)
