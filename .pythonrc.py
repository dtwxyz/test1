import sys, os, pydoc, pprint
builtin_module = sys.modules['__main__'].__builtins__
setattr(builtin_module, 'sys', sys)
setattr(builtin_module, 'os', os)
setattr(builtin_module, 'pydoc', pydoc.doc)
setattr(builtin_module, 'pprint', pprint.pprint)
del pydoc, pprint

##########################################################
# for interactive python not getting HOME in env, e.g.,
#   pants repl
#   pants test.pytest --options='--pdb'
# run
# import os
# with open(os.path.expanduser('~/.pythonrc.py')) as pyrc:
#   exec(pyrc.read())

import readline
readline.read_init_file(os.path.expanduser('~/.inputrc'))

#############
# for python2

import rlcompleter

#####################
# history for python2

history_file = os.path.expanduser('~/.python_history')

def save_history(history_file = history_file):
    import readline
    readline.write_history_file(history_file)

setattr(builtin_module, 'save_history', save_history)

import atexit
#atexit.register(save_history)

if os.path.exists(history_file):
    import readline
    readline.read_history_file(history_file)

#####################
# history for python3

import readline
if hasattr(readline, 'set_auto_history'): readline.set_auto_history(False)

#####################
# virtual environment

if 'VIRTUAL_ENV' in os.environ:
    import virtualenv
    setattr(builtin_module, 'virtualenv', virtualenv)
    activate_this = os.path.join(os.environ['VIRTUAL_ENV'], 'bin/activate_this.py')
    exec(open(activate_this).read(), dict(__file__ = activate_this))

##########################################
# copy sys.path between interactive python

syspath_file = '~/tmp/syspath.py'

def save_syspath(syspath_file = syspath_file):
    import sys, os
    with open(os.path.expanduser(syspath_file), 'w') as f:
        f.write(repr(sys.path))
        f.flush()

def read_syspath(syspath_file = syspath_file):
    import sys, os
    with open(os.path.expanduser(syspath_file)) as f:
        for p in eval(f.read()):
            if p not in sys.path:
                sys.path.insert(0, p)

setattr(builtin_module, 'save_syspath', save_syspath)
setattr(builtin_module, 'read_syspath', read_syspath)

del builtin_module
