# CPEXUTIL External Access Layer (EAL)
# Access utilities from other modules
# When using Impor, remember to ALWAYS put quotes around the module name!

def impor(mod):
    thing = __import__(mod)
    globals().update(thing.__dict__)

os.chdir("..")
impor("CP-Extended-Utils")
os.chdir(f"{os.getcwd}/CP-Extended-Utils")

