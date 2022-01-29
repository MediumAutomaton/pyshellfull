#AUI (ASCII-UI) - The Plain-Text UI for CP
#Uses 1 TTY for All User I/O
#Fully Compatible & Tested for: [CP 0.8, CPFM 1.0 standalone]

class CPUI:
    def __init__(self, args, comms=None):
        self.comms = comms
        self.version = "1.1-1 standalone"
        self.log = args.log
        self.cplog = open("cplog.txt", "r+")
        self.debug("Debug messages look like this")
        self.debug(f"AUI version {self.version}")

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
        self.say(list(self.comms))

if __name__ == "__main__":
    print("This is a CP-UI module, made to be imported into CP's ustart mode or other projects requiring a CP-UI module.")