# pyshellfull
----
### "Command Processor" (CP) Shell - An introductory project for myself (very incomplete)
- I am new to everything, including Markdown. Sorry in advance for the complete buggy mess of this project.
- Anyway, it's shared here now if you're interested.
- I don't ever have much time to work on this.
- I will get the GPL commands in there as soon as possible.

### There is a "CP-Extended-Utils" folder - everything in there is on hold for now until the main project (cpt2.py) hits version 1.0.
Oddities:
- "#cpfm.py" - That's a standalone version, but I'm still turning it into the version to be used with the shell. It will disappear eventually.

## To launch this program:
- Simply launch cpt2.py in python3. Note that this project is written in Python 3.9.5. I think 3.6 should work, but I haven't tested it.
- The debug console comes up in a TkInter window by default. If you do not have a window manager running (text-only), then start with the "-c" argument for text-only.

I am working on a list of specifications for this program to adhere to. Find it as "cpt2spec.md" in the Docs folder.

#### Version Numbering
Versions are numbered as follows:
Major.Minor-Patch

- Major increments come with a dramatic change in the software's operation, where users and developers of modules for this shell will not be able to carry their experience with previous major versions forward. These coincide with new specification releases. (CP 1.x is CPT2, CP 2.x will be CPT3)
- Minor increments come with added features which do not affect the rest of the program or modules developed for it. Users can bring all of their prior experience forward to the new version, only learning the new features.
- Patches are simple bugfixes and nothing more. If a bugfix becomes rather complex, it will probably create a new minor version.
