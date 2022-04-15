"""
Command-module loader for Kaldi.

This script is based on 'dfly-loader-wsr.py' written by Christo Butcher and
has been adapted to work with the Kaldi engine instead.

This script can be used to look for Dragonfly command-modules for use with
the Kaldi engine. It scans the directory it's in and loads any ``_*.py`` it
finds.
"""


# TODO Have a simple GUI for pausing, resuming, cancelling and stopping
# recognition, etc

from __future__ import print_function
import os.path
import logging, subprocess, sys

from dragonfly import RecognitionObserver, get_engine
from dragonfly import Grammar, MappingRule, Function, Dictation, FuncContext, ActionBase
from dragonfly.loader import CommandModuleDirectory
from dragonfly.log import setup_log

from sounddevice import query_devices


# --------------------------------------------------------------------------
# Set up basic logging.

if False:
    # Debugging logging for reporting trouble
    logging.basicConfig(level=10)
    logging.getLogger('grammar.decode').setLevel(20)
    logging.getLogger('grammar.begin').setLevel(20)
    logging.getLogger('compound').setLevel(20)
    logging.getLogger('kaldi.compiler').setLevel(10)
else:
    setup_log()
    # logging.getLogger('kaldi.compiler').setLevel(2)


# --------------------------------------------------------------------------
# User notification / rudimentary UI. MODIFY AS DESIRED

# For message in ('sleep', 'wake')
def notify(*text):
    print(*text)
    subprocess.run(['notify-send', ' '.join(text)])

# --------------------------------------------------------------------------
# Sleep/wake grammar.

sleeping = False

def load_sleep_wake_grammar(initial_awake):
    sleep_grammar = Grammar("sleep")

    def sleep(force=False):
        global sleeping
        if not sleeping or force:
            sleeping = True
            sleep_grammar.set_exclusiveness(True)
        notify('Sleeping...')

    def wake(force=False):
        global sleeping
        if sleeping or force:
            sleeping = False
            sleep_grammar.set_exclusiveness(False)
        notify('Awake...')

    def halt(force=False):
        exit(0)

    class SleepRule(MappingRule):
        mapping = {
            'dragonfly exit': Function(halt),
        "start listening":  Function(wake) + Function(lambda: get_engine().start_saving_adaptation_state()),
            "stop listening":   Function(lambda: get_engine().stop_saving_adaptation_state()) + Function(sleep),
            "halt listening":   Function(lambda: get_engine().stop_saving_adaptation_state()) + Function(sleep),
        }
    sleep_grammar.add_rule(SleepRule())

    sleep_noise_rule = MappingRule(
        name = "sleep_noise_rule",
        mapping = { "<text>": Function(lambda text: False and print(text)) },
        extras = [ Dictation("text") ],
        context = FuncContext(lambda: sleeping),
    )
    sleep_grammar.add_rule(sleep_noise_rule)

    sleep_grammar.load()

    if initial_awake:
        wake(force=True)
    else:
        sleep(force=True)


def load_noise_grammar():
    noise_grammar = Grammar("noise")

    noise_grammar.add_rule(MappingRule(
        name='noise',
        mapping = { "<text> {weight=10}": Function(lambda text: print('Noise: ', text)) },
        extras = [ Dictation("text") ],
    ))

    noise_grammar.load()

# --------------------------------------------------------------------------
# Simple recognition observer class.

class Observer(RecognitionObserver):
    def on_begin(self):
        # notify("Speech started.")
        pass

    def on_recognition(self, words):
        notify("Recognized:", " ".join(words))

    def on_failure(self):
        print("Sorry, what was that?")


# --------------------------------------------------------------------------
# Main event driving loop.

def main():
    logging.basicConfig(level=logging.INFO)

    try:
        path = os.path.dirname(__file__)
    except NameError:
        # The "__file__" name is not always available, for example
        # when this module is run from PythonWin.  In this case we
        # simply use the current working directory.
        path = os.getcwd()
        __file__ = os.path.join(path, "kaldi_module_loader_plus.py")

    if 'devices' in sys.argv:
        print('microphones:', get_engine('kaldi').print_mic_list())
        exit(0)
    # Set any configuration options here as keyword arguments.
    if 'test' in sys.argv:
        engine = get_engine('text')
    else:
        for d in query_devices():
            mic = None
            if len([preferred for preferred in ["Blue", "Meteor", "webcam"] if preferred in d['name']]) > 0:
                mic = d['name']
                print('Using', mic)
                break
        if mic is None:
            print('None of your prefered microphones are installed!')
            print(query_devices())
            exit()
        engine = get_engine("kaldi",
            model_dir='kaldi_model',
            # tmp_dir='kaldi_model_zamia.tmp',  # default for temporary directory
            # vad_aggressiveness=3,  # default aggressiveness of VAD
            # vad_padding_start_ms=300,  # default ms of required silence before VAD
            vad_padding_end_ms=500,  # default ms of required silence after VAD
            # vad_complex_padding_end_ms=500,  # default ms of required silence after VAD for complex utterances
            audio_input_device=mic,
            # auto_add_to_user_lexicon=True,  # set to True to possibly use cloud for pronunciations
            # lazy_compilation=True,  # set to True to parallelize & speed up loading
            # cloud_dictation=None,  # set to 'gcloud' to use cloud dictation
        )

    # Call connect() now that the engine configuration is set.
    engine.connect()

    # Register a recognition observer
    observer = Observer()
    observer.register()

    load_sleep_wake_grammar(True)
    # load_noise_grammar()

    directory = CommandModuleDirectory(path, excludes=[__file__])
    directory.load()

    # Start the engine's main recognition loop
    if 'test' not in sys.argv:
        engine.prepare_for_recognition()
    try:
        # Loop forever
        print("Listening...")
        engine.do_recognition()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
