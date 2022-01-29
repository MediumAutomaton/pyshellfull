#CPEXUTIL Diagnostic script
#Suspicious that you're not loading CP properly, or that you've found a CP bug?
#Use this to find out! This version designed to test CPT2.
#In the process, also tests this package's __init__.py file to some extent.

def impor(mod):
    thing = __import__(mod)
    globals().update(thing.__dict__)

impor("__init__")
try:
    if Utils:
        if ui:
            if Commands:
                return True
except Exception as x:
    print(f"[CEUdiag] Failed: {x}")
    return false
