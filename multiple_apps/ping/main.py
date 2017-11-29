import getopt
import pkg_resources
import sys

import ping.pinger


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
    verbose = False
    try:
        opts, args = getopt.getopt(argv[1:], "v?")
    except:
        usage("Bad option.  Just -v and -? accepted")
    for o, a in opts:
        if o == "-v":
            verbose = True
        else:
            usage()
    ping.pinger.pinger(settings, args, verbose)

if __name__ == "__main__":
    # This is for testing, so use test values
    test_settings = { "version": "v0.1" }
    configure(test_settings)
    main(sys.argv)

