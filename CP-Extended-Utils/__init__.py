# CP Extended Utilities Package v0.1-0
# Three distinct stages for this script, marked by comments above each one:
# Initialize; Import Utilities; Finalize


def impor(mod):
    thing = __import__(mod)
    globals().update(thing.__dict__)

# List the utilities to be imported into CP below.
mods = [
    "cpfm",
    "cpcoolborder",
    "ceudiag",
]

# Initialize
newcomms = {}
# Provide the same Python modules as CP
import os
import sys
import time
import shlex
from tkinter import *
# End of Python built-ins

os.chdir(f'{os.getcwd()}/CP-Extended-Utils')
print(os.getcwd())
pendingcomms = {}

# Import Utilities
for mod in mods:
    impor(mod)
    pendingcomms.update(newcomms)

# Finalize
impor("cpt2")
newcomms = pendingcomms
if ceu.cpt2test():
    ui.debug("[cpexutil] CP-Extended-Utils successfully loaded.")
