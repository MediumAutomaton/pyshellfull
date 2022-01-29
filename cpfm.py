#CPFM Module v1.0-0
#Contains the CPFM functions to be imported into CP 1.0 or compatible.
#Currently requires an external CPUI module; trying to use CP's UI behaves weirdly and is currently not working.

# CPFM starts here.
import os
import sys
from pathlib import Path


p = Path()
global cargs

def rawSee(x):
    try:
        with open(x) as f:
            ui.say(f.read())
    except FileNotFoundError:
        ui.say("Not found!")
    except PermissionError:
        ui.say("Permission denied.")
    except Exception as x:
        ui.debug(f"Error: {x}")
        ui.say("Couldn't see file.")

def changeDir(new):
    try:
        os.chdir(f'{os.getcwd()}/{new}')
    except FileNotFoundError:
        ui.say("Not found!")
    except PermissionError:
        ui.say("Permission denied.")
    except NotADirectoryError:
        ui.say("Not a directory!")
    except Exception as x:
        ui.debug(f"Error: {x}")

def getLast(x):
    return str(x).split("/")[-1]

def showDir():
    try:
        pi = [x for x in p.iterdir()]
        dirs = []
        other = []
        for x in pi:
            if x.is_dir():
                dirs.append(x)
        for x in pi:
            if not x.is_dir():
                other.append(x)
        for x in dirs:
            ui.say(f"[dir] {getLast(x)}")
        for x in other:
            ui.say(getLast(x))
    except PermissionError:
        ui.say("Permission denied.")
    except Exception as x:
        ui.debug(f"Error: {x}")
        ui.say("Couldn't show directory.")

def makeFile(new):
    try:
        with open(new, "x"):
            pass
    except PermissionError:
        ui.say("Permission denied.")
    except FileExistsError:
        ui.say("File already exists.")

def makeDir(new):
    try:
        os.mkdir(new)
    except PermissionError:
        ui.say("Permission denied.")
    except FileExistsError:
        ui.say("Directory already exists.")

def remove(file):
    try:
        os.remove(file)
    except PermissionError:
        ui.say("Permission denied.")

global cargs
newcomms = {
"show": "showDir()",
"change": "changeDir(cargs[0])",
"see": "rawSee(cargs[0])",
"makefile": "makeFile(cargs[0])",
"makedir": "makeDir(cargs[0])",
"remove": "remove(cargs[0])"
}

def impor(mod):
    thing = __import__(mod)
    globals().update(thing.__dict__)
    
impor("auinodebug")
ui = CPUI()
ui.say("cpfm running")
