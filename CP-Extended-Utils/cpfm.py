#CPFM Module v1.0-0
#Contains the CPFM functions to be imported into CP 1.0 or compatible.

# CPFM starts here.
import os
import sys
from pathlib import Path

newcomms = {
            "show": "self.showDir()",
            "change": "self.changeDir(self.arg)",
            "see": "self.seeFile(self.arg)",
            "makefile": "with open(self.arg): pass",
            "exit": "sys.exit(2)",
            "help": "ui.say(list(self.comms))",
            "makedir": "os.mkdir(self.arg)",
        }

class CPFM:
    def __init__(self):
        self.p = Path()
        self.command = ""
        self.arg = ""
        global newcomms
        self.comms = newcomms

    def launch(self):
        while True:
            try:
                self.command = ui.ask(os.getcwd())
                self.arg = " ".join(self.command.split()[1:len(self.command)])
                self.command = self.command.split()[0]
                exec(self.comms[self.command])
            except Exception as x:
                ui.say("Unknown command or missing arguments.")
                ui.debug(x)

    def seeFile(self, x):
        with open(x) as f:
            lines = f.readlines()
            if ui.ask("Squeeze output?"):
                ui.say(lines)
            else:
                for item in lines:
                    ui.say(item)

    def changeDir(self, new):
        try:
            os.chdir(f'{os.getcwd()}/{self.arg}')
        except FileNotFoundError as x:
            ui.say("Not found!")
            ui.debug(x)
        except PermissionError:
            ui.say("Permission denied.")
        except NotADirectoryError:
            ui.say("Not a directory!")
        except Exception as x:
            ui.debug(f"Error: {x}")

    def getLast(self, x):
        return str(x).split("/")[-1]

    def showDir(self):
        pi = [x for x in self.p.iterdir()]
        dirs = []
        other = []
        for x in pi:
            if x.is_dir():
                dirs.append(x)
        for x in pi:
            if not x.is_dir():
                other.append(x)
        for x in dirs:
            ui.say(f"[dir] {self.getLast(x)}")
        for x in other:
            ui.say(self.getLast(x))