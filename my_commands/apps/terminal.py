from dragonfly import Dictation, AppContext, Text, Key, IntegerRef, Function
from breathe import Breathe, CommandContext
import subprocess

context = CommandContext("terminal")

def notify(*text):
    print(*text)
    subprocess.run(['notify-send', ' '.join(text)])
Breathe.add_commands(
    # Commands will be active either when we are editing a python file
    # or after we say "enable python". pass None for the commands to be global.
    # context = AppContext(title=".py") | CommandContext("python"),
    context = AppContext(executable='terminal') | context,
    mapping = {
        'window new': Key('cs-n'),

        'git diff': Text('git diff\n'),
        'git pull': Text('git pull\n'),
        'git log': Text('git log --graph\n'),
        'git push': Text('git push\n'),
        'git status': Text('git status\n'),
        'git add': Text('git add '),
        'git commit minus a m <text>': Text('git commit -am "%(text)s"')+Key('left'),
        'git commit minus m <text>': Text('git commit -m "%(text)s"')+Key('left'),
        'git <text>': Function(lambda text: notify('unrecognized git command:', str(text))),
        
        'cargo build': Text('cargo build\n'),
        'cargo build release': Text('cargo build --release\n'),
        'cargo test': Text('cargo test\n'),
        'cargo check': Text('cargo check\n'),
        'cargo bench': Text('cargo bench\n'),
        'cargo outdated': Text('cargo outdated -R\n'),
        'cargo tarpaulin': Text('cargo tarpaulin\n'),

        'r q': Text('rq\n'),
        'r q run': Text('rq run '),
        'r q cancel all': Text('rq cancel --all\n'),

        'codium here': Text('code -n --folder-uri `pwd` &\n'),

        'cd': Text('cd '),

        'control c': Key('c-c'),
        'complete me': Key('tab'),
        'repeat last command': Key('up')+Key('enter'),
    },
    extras = [
        IntegerRef("n", 1, 20, default=1),
        Dictation("text", default=""),
    ]
)
