#This version compatible with CPT2 protocol (CP 0.9 or compatible)

#Encase your terminal output in neat, configurable borders!
#Can import borders from a file or can use the options below.
#Import this module and call its functions from your program!
#Version 1.0-0

#Terminal dimensions
rows = 48
cols = 116

#Top/Bottom Borders of coolBorder messages
cbh = "="
#Left Side
cbvl = "///"
#Right Side (There's some cheating going on here to make the backslashes work.)
a = ""
cbvr = f"\\{a}\\{a}\{a}"

#CPT2 Compatibility Layer
newcomms = {
"coolBorder":"",
}

def msgSplit(msg):
    global cols
    if len(msg) > cols:
        ref = cols
        idx1 = cols-(ref*2)
        idx2 = cols-ref
        out = []
        while idx2 < len(msg):
            idx1 = idx1 + ref
            idx2 = idx2 + ref
            out.append(msg[idx1:idx2])
        return out

def msgBorder(msg):
        global cbvl
        global cbvr
        global cbh
        split = msgSplit(msg)
        border = ""
        print(len(split[1]))
        for i in split[1]:
            border = border + cbh
        print(border)
        for i in split:
            print(f"{cbvl}{i}{cbvr}")
        print(border)