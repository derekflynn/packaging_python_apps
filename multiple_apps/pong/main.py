import getopt
import pkg_resources
import sys

import pong.ponger


settings = None

def configure(new_settings):
    global settings
    settings = new_settings

def usage(message=None):
    if message:
        sys.stderr.write("{}\n\n".format(message))
    sys.stderr.write(pkg_resources.resource_string(__name__, "USAGE.txt"))
    sys.stderr.write("\n")
    sys.exit(1)

def main(argv):
    log_file = "/dev/stdout"
    try:
        opts, args = getopt.getopt(argv[1:], "l:?")
    except:
        usage("Bad option.  Just -l log_file and -? accepted")
    for o, a in opts:
        if o == "-l":
            log_file = a
        else:
            usage()
    pong.ponger.ponger(settings, log_file)

if __name__ == "__main__":
    # This is for testing, so use test values
    test_settings = { "version": "v0.1" }
    configure(test_settings)
    main(sys.argv)

