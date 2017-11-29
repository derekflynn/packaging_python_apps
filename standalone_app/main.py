import getopt
import pkg_resources
import sys
import yaml
import app.feature


def usage(message=None):
    if message:
        print(message)
    print(pkg_resources.resource_string(__name__, "README.txt"))
    sys.exit(1)

def configure(app):
    config = yaml.load(pkg_resources.resource_stream(__name__, "config.yml"))
    if app not in config:
        usage("Bad configuration -- should have '{}' section".format(app))
    return config[app]

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
    config = configure("app")
    app.feature.hello(config, verbose)

if __name__ == "__main__":
    main(sys.argv)

