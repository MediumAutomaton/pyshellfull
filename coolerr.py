# Add some cool errors when CP crashes!
# Or see a random error without crashing using the included err command.

#allerr = '\n'.join(list(err[i] for i in list(err)))
newcomms = {"err":"ui.say(err[randint(1, len(list(err)))])"}

#ui.say(list(err[i] for i in list(err)))

newErr = {
    6:"CP doesn't have a bugtracker! To fail to report this crash, go to-\nProcess finished with Exit Code 2.",
    11:"=================\n|||Too Cool :(|||\n================="
}