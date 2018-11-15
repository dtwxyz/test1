#!/usr/bin/env python
import os, sys
with open(os.path.expanduser(os.environ['PYTHONSTARTUP'])) as pyrc:
    exec(pyrc.read())
    del pyrc
read_syspath()
os.environ['PYTHONPATH'] = ':'.join(sys.path)
sys.argv.insert(1, '--color=no')
os.execvp('pytest', sys.argv)
