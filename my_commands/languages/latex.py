from dragonfly import Dictation, AppContext, Text, Key, \
     Function, Choice, Integer
from breathe import Breathe, CommandContext, Exec, CommandsRef

def start_inline():
    latex_context.disable()
    inline_context.enable()
def end_math():
    inline_context.disable()
    latex_context.enable()

latex_context = CommandContext("latex")
inline_context = CommandContext("inline math")
Breathe.add_commands(
    context = latex_context,
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
}
# fraction sin x ^2squared divided by 3 + x
#  \frac{\sin(x^2)}{3+x}
function_mapping = {
  k:Text('\\'+f+'{') + Exec("expr") + Text('}')
      for k,f in functions.items()
}
Breathe.add_commands(
    context = inline_context,
    mapping = {
      "frac <expr1> over <expr2>":
          Text("\\frac{") + Exec("expr1") + Text("}{") + Exec("expr2") + Text("}"),
      "of <expr1>":
          Text("\\left(") + Exec("expr1") + Text("\\right)"),
    },
    extras = [
        CommandsRef("expr1", 8),
        CommandsRef("expr2", 8),
    ],
    top_level=True,
)
# Breathe.add_commands(
#     context = inline_context,
#     mapping = function_mapping,
#     extras = [
#         CommandsRef("expr", 8),
#     ],
#     top_level=True,
# )
variable = Choice("variable", {
        "psi": r"\psi",
        "phi": r"\phi",
        "big psi": r"\Psi",
        "pi": r"\pi",
        "k": r" k",
        "x": r" x",
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
