cargs = "You forgot your command arguments!"
conftemp = '#Syntax version of this config file.\nsyntaxver = "1.1-0"\n#After updating CP, you might want to delete this file and have CP generate a new one conforming to the newer syntax standards.\n#Below are some config options. They are Python lists; be sure to use correct syntax.\n#Disabled commands:\ndiscomm = []\n#Automatically import modules:\nimpor = []\n#Run commands on startup:\nautorun = []\n\ndef main():\n    print(f"CP Config File; Syntax version {syntaxver}.")\n    print("To change config settings, edit this Python file in a text editor.")\n\nnewcomms = {}\n\nif __name__ == "__main__":\n    main()'
version = "0.9-5"
exinfo = "Copyleft 2021; licensed under GNU GPL 3.0 (should work for now, though I have yet to read the license)"
comms = {"ver": "self.commands.ver()", "debug": "self.commands.debug()", "merge": "self.commands.impor()", "help": "self.commands.help()", "exec": "self.commands.exec()", "read": "self.commands.read()", "echo": "self.commands.echo()", "testfile": "self.commands.testFile()", "readlog": "self.commands.readLog()", "eval": "self.commands.eval()", "exit": "self.commands.exit()", "coolBorder": "self.commands.coolBorder()", "scrip": "self.commands.scrip()",}
err = {1:"Kaboom!", 2:"Uh-oh...", 3:":(", 4:"Explicable Error Message", 5:"Who programmed this mess?", 6:"CP doesn't have a bugtracker! To fail to report this crash, go to-", 7:"Congratulations! You have found one of many CP-crashing bugs, either in CP or the applications written for it.", 8:"Today is your unlucky day!", 9:"Traceback(most recent call last):\nCP crashed. :(", 10:"Can't wait for CP 0.9-1142! By then they'll have fixed ALL the problems!"}


class AUI:
    #ASCII-UI - Plain-Text UI for CP - only used in cstart mode.
    def __init__(self, args):
        self.version = "1.1-0"
        self.log = args.log
        self.cplog = open("cplog.txt", "r+")
        self.debug("Errors look like this")
        self.debug("AUI version {self.version}; you're running cstart mode!")
    
    def debug(self, msg):
        self.say(f"!!{msg}!!")
        if self.log:
            self.cplog.write(msg)

    def readLog(self):
        return self.cplog.read()

    def say(self, msg):
        print(msg)

    def ask(self, msg=""):
        return input(msg + ":")

    def hlp(self):
        self.say(list(comms))
        ui.say("Exec and Eval don't take arguments; it will prompt you for what to execute after being called. This allows for function calls that the argument parsing might normally interfere with.\nScrip ALWAYS needs an argument; type 'scrip h' for help")

class HUI:
    #CP-standard HybridUI: tty User Interaction; TkInter Debug Console.
    def __init__(self, args):
        self.log = args.log
        self.cplog = open("cplog.txt", "r+")
        self.root = Tk()
        self.root.title(f"CP {version} Debug Console")
        self.log = ScrolledText(height=10, wrap=WORD, state=NORMAL)
        self.log.pack(fill=BOTH, expand=True)
        self.debug("Debug console initialized.")
    
    def debug(self, msg):
        l = self.log
        l.insert(END, f"\n{msg}")
        l.yview_moveto(1.0)
        self.root.update()
        if self.log:
            self.cplog.write(msg)

    def readLog(self):
        return self.cplog.read()

    def say(self, msg):
        print(msg)

    def ask(self, msg=""):
        return input(msg + ":")

    def hlp(self):
        ui.say(list(comms))
        ui.say("Exec and Eval don't take arguments; it will prompt you for what to execute after being called. This allows for function calls that the argument parsing might normally interfere with.\nScrip ALWAYS needs an argument; type 'scrip h' for help")
            
class Commands:
    def __init__(self):
        self.utils = Utils()

    def ver(self):
        ui.say(version)
        ui.say(exinfo)

    def debug(self):
        ui.debug(" ".join(cargs))

    def impor(self):
        self.utils.impor(" ".join(cargs))

    def help(self):
        ui.hlp()

    def exec(self):
        try:
            exec(ui.ask("Exec"))
        except Exception as x:
            ui.say("Problem executing. Make sure you've typed the function correctly.")
            ui.debug(f"Could not execute. Error:\n{x}")

    def eval(self):
        try:
            ui.say(eval(ui.ask("Eval")))
        except Exception as x:
            ui.say("Couldn't evaluate. Make sure you've typed the expression correctly.")
            ui.debug(f"Could not evaluate. Error:\n{x}")

    def read(self):
        ui.say("Coming soon!")

    def echo(self):
        ui.say(" ".join(cargs))

    def testFile(self):
        file = cargs
        try:
            with open(file, "r"):
                ui.say("Pass! File opened successfully.")
        except Exception as x:
            ui.say(f"File '{file}' could not be opened.")

    def readLog(self):
        ui.readLog()

    def coolBorder(self):
        ui.say(Utils.coolBorder(" ".join(cargs)))

    def scrip(self):
        Utils.scrip()

    def exit(self):
        ui.debug("CP is safely exiting. It (probably) didn't crash.")
        ui.say(f"Thanks for using CP {version}!")
        time.sleep(1)
        sys.exit(2)


class CP:
    def __init__(self, args):
        self.ver = args.version
        self.conf = args.regenconf
        self.commands = Commands()
        self.utils = Utils()
        print(version, exinfo)
        if self.ver:
            exit()
        if self.conf:
            self.makeConfig()

    def start(self):
        self.discomm = discomm
        while True:
            try:
                user = ui.ask()
                user = shlex.split(user)
                command = user[0]
                global cargs
                cargs = user[1:len(user)]
                if command:
                    if command == "#>:)":
                        ui.say("#>:)")
                        ui.debug("#>:)")
                        break
                    if command in discomm:
                        ui.say("Couldn't process command.")
                        ui.debug(f"User tried to run disabled command {command}.")
                    elif command in list(comms):
                        exec(comms[command])
                    else:
                        ui.say(eval(command))
            except Exception as x:
                ui.say("Couldn't process command.")
                ui.debug(f"Failed to process command {command}. Error:\n{x}")
        raise InterruptedError


    #CP Launcher
    def config(self):
        try:
            self.utils.impor("cpconf")
            assert syntaxver == "1.1-0"
        except Exception as x:
            ui.debug(f"Problem with the config file:\n{x}\nCreating new 'cpconf.py' from built-in template.")
            self.makeConfig()
        try:
            for item in impor:
                self.utils.impor(item)
        except Exception as x:
            ui.debug(f"Problem with auto-import of modules listed in cpconf. Error:\n{x}")
        try:
            for item in autorun:
                exec(comms[item])
        except Exception as x:
            ui.debug(f"Could not autorun all commands. Error:\n{x}")
        
    def makeConfig(self):        
        with open("cpconf.py", "x"):
            pass
        with open("cpconf.py", "r+") as self.conf:
            self.conf.write(conftemp)

    def launch(self):
        try:
            self.utils.impor("cpexutil")
        except Exception as x:
            ui.say("CP Extended Utilities not detected! We recommend the 'cpexutil' module to make CP easier to use.")
            ui.debug(f"CP Extended Utilities couldn't be imported:\n{x}")
        try:
            ui.debug("Attempting launch...")
            self.config()
            self.start()
        except Exception as x:
            ui.debug(f"{err[randint(1, 10)]} Error:\n{x}")
            ui.say(err[randint(1, 10)])
            sys.exit(2)

class Utils:
    #Built-in Utilities - CP requires these!
    #They are Impor {called by impor([module-name])} and End {end()}.
    #Impor imports modules, and End allows exiting from alternate shells if necessary.
    @staticmethod
    def impor(mod):
        try:
            thing = __import__(mod)
            globals().update(thing.__dict__)
            p = f"Imported module {mod}."
            ui.say(p)
            ui.debug(p)
            try:
                comms.update(newcomms)
            except Exception as x:
                ui.say(
                    f"Module {mod} imported, but commands couldn't be gathered. Commands in the imported module must be called directly.")
                ui.debug(f"[Impor] Problem merging new commands for {mod} (most likely a non-CP module):\n{x}")

        except Exception as x:
            ui.say(f"Couldn't import module '{mod}'.")
            ui.debug(f"[Impor] Problem importing module {mod}:\n{x}")

    @staticmethod
    def coolBorder(arg):
        global cbvl
        global cbvr
        global cargs
        msg = f"{cbvl}{arg}{cbvr}"
        border = ""
        global cbh
        for i in msg:
            border = border + cbh
        return(f"{border}\n{msg}\n{border}")

    @staticmethod
    def lock():
        ui.ask("Enter anything to continue...")
        global comms
        comms = {"lock":"raise NotImplementedError"}
        while True:
            exec(comms[lock])

    @staticmethod
    def end():
        ui.say("Confirm kill app?") 
        i = input("[y/n]:")
        if i in ("Y", "y", "Yes", "yes"):
            return True

    @staticmethod
    def scrip():
        if cargs[0] == "f":
            with open(f"{cargs[1]}.scrip", "x"):
                newscrip = {f"{cargs[1]}":f"Utils.scripread({cargs[1]})"}
                global comms
                comms.update(newscrip)
            with open(cargs[1], "w") as f:
                f.write("[]")
        elif cargs[0] == "a":
            with open(cargs[1], "w") as f:
                f.seek(0, len(f.read())-1)
                f.write(f"{cargs[2]}, ")
        elif cargs[0] == "d":
            os.remove(f"{cargs[1]}.scrip")
        elif cargs[0] == "s":
            p = Path(".")
            l = list(p.glob("**/*.scrip"))
            for i in l:
                ps = {i: f"scripread({i})"}
                comms.update(ps)
        elif cargs[0] == "r":
            Utils.scripread(cargs[1])
        else:
            ui.say("f [scripname]: create and install new scrip\na [scripname] [toAppend]: append to scrip\nd [scripname]: delete scrip\nr [scripname]: install scrip (add it to the CP command dictionary)\ns: find and install all scrips in current working directory")

    @staticmethod
    def scripread(file):
        with open(f"{file}.scrip", "r") as f:
            l = f.read()
            for i in l:
                try:
                    exec(comms[i])
                except Exception as x:
                    ui.debug(f"Script: {file}\nError: {x}")
                    ui.say("Error running script.")

#Top-Level
print(__name__)
import os
import sys
import time
import shlex
from pathlib import Path
from random import randint
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-ver", "--version", help="Show program version then exit.", action="store_true")
parser.add_argument("-c", "--cstart", help="Use only plain-text. (AUI instead of HUI) If running without a graphical environment (standard tty only) you MUST use this mode!", action = "store_true")
parser.add_argument("-l", "--log", help="Log all debug messages to a text file. Also adds date codes to console initializations and time codes to messages.", action="store_true")
parser.add_argument("-r", "--regenconf", help="Generate new 'cpconf.py' then exit.", action="store_true")
parser.add_argument("-u", "--ustart", help="Use a different CP-UI module.", action="store_true")
parser.add_argument("-e", "--errpack", help="Want to use an errorpack, to make the rare CP crash even funnier?", action="store_true")
args = parser.parse_args()
if args.cstart:
    ui = AUI(args)
elif args.ustart:
    thingy = input("CP-UI Module Name:")
    Utils.impor(thingy)
    ui = CPUI(args)
else:
    from tkinter import *
    from tkinter.scrolledtext import ScrolledText
    ui = HUI(args)

if args.errpack:
    thingy = input("Errpack Module Name:")
    Utils.impor(thingy)
    err.update(newErr)

CP = CP(args)
CP.launch()
