from dragonfly import Dictation, AppContext, Text, Function, Choice, DictList, DictListRef, Integer, Key
from breathe import Breathe, CommandContext, Exec, CommandsRef

def start_math():
    math_commands.clear()
    math_commands.update({
        'square root': Text(r'\sqrt'),
        'sine': Text(r'\sin'),
        'cosine': Text(r'\cos'),
        'tangent': Text(r'\tan'),
        'exponential': Text(r'\exp'),
        'log': Text(r'\ln'),
        'end math': Function(lambda: math_commands.clear()),

        "psi": Text(r"\psi"),
        "phi": Text(r"\phi"),
        "big psi": Text(r"\Psi"),
        "pi": Text(r"\pi"),
        "gamma": Text(r"\gamma"),

        "foxtrot": Text(r" f"),
        "india": Text(r" i"),
        "j": Text(r" j"),
        "k": Text(r" k"),
        "x": Text(r" x"),
        "y": Text(r" y"),
        "z": Text(r" z"),
        'squared': Text('^2'),
        'plus': Text('+'),
        'minus': Text('-'),
        'cross': Text(r'\times'),
        'times': Text(r'\times'),
        'dot product': Text(r'\dot'),

        'fraction': Text(r'\frac{}{}') + Key('left:3'),
        # 'to the <nth>': Text('^%(nth)s'),
    })
math_commands = DictList('math_commands')

def process_math_command(math_command):
    math_command.execute()

def start_inline():
    start_math()
    math_commands['end math'] = Text('$ ')+Function(lambda: math_commands.clear())
    math_commands['end inline'] = Text('$ ')+Function(lambda: math_commands.clear())
def start_align():
    start_math()
    math_commands['end math'] = Text('\n\\end{align}\n')+Function(lambda: math_commands.clear())
    math_commands['end align'] = Text('\n\\end{align}\n')+Function(lambda: math_commands.clear())
def end_math():
    math_commands.clear()


context = CommandContext("latex")
Breathe.add_commands(
    context=AppContext(title='.tex') | context,
    mapping={
        'new paragraph': Text('\n\n'),
        'emphasize <latex>': Text(r'\emph{}%(latex)s}\n'),
        'inline math': Text('$')+Function(start_inline),
        'begin align': Text('\\begin{align}\n')+Function(start_align),
        'begin math': Function(start_math),
        # 'stop math': Function(end_math),
        "<math_command>": Function(process_math_command),
    },
    extras=[
        DictListRef('math_command', math_commands),
        Dictation("latex", default="").lower().replace(" new paragraph ", "\n\n"),
    ]
)

# fraction sin x ^2squared divided by 3 + x
#  \frac{\sin(x^2)}{3+x}
# Breathe.add_commands(
#     context=context,
#     mapping={
#        "<expr1> frac <expr2> over <expr3>":
#             Exec("expr1") + Text("\\frac{") + Exec("expr2") + Text("}{") + Exec("expr3") + Text("}"),
#        "<expr1> over <expr2>":
#            Text("\\frac{") + Exec("expr1") + Text("}{") + Exec("expr2") + Text("}"),
#        "<expr1> of <expr2>":
#            Exec("expr1") + Text("\\left(") + Exec("expr2") + Text("\\right)"),
#        "<expr1> e to the <expr2>":
#            Exec("expr1") + Text(" e^{") + Exec("expr2") + Text("}"),
#         'end math': Text('$')+Function(end_math),
#     },
#     extras = [
#         CommandsRef("expr1", 8),
#         CommandsRef("expr2", 8),
#         CommandsRef("expr3", 8),
#     ],
#     top_level=True,
# )
variable = Choice("variable", {
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
# math_mapping = {}
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
# for k,v in math_mapping.items():
#     inline_mapping[k] = v
# for k,v in functions.items():
#     inline_mapping[k] = Text(v)
# Breathe.add_commands(
#     context = inline_context,
#     mapping = inline_mapping,
#     extras = [
#         Dictation("snaketext", default="").lower().replace(" ", "_"),
#         Dictation("screamingsnaketext", default="").upper().replace(" ", "_"),
#         Dictation("CamelText", default="").title().replace(" ", ""),
#         variable,
#         nth,
#         Integer('n', 0, 300),
#     ]
# )
