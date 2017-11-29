import importlib
import pkg_resources
import sys
import yaml


def usage(message=None):
    if message:
        print(message)
    print(pkg_resources.resource_string(__name__, "README.txt"))
    sys.exit(1)

def main(argv):
    config = yaml.load(pkg_resources.resource_stream(__name__, "config.yml"))
    if len(argv) < 2:
        usage("No application specified")
    application = argv[1]
    if application not in config:
        usage("No section for application '{}'".format(application))
    section = config[application]
    if "module" not in section or "config" not in section:
        usage("No module and config for application '{}'".format(application))
    module_name = section["module"]
    configuration = section["config"]
    module = importlib.import_module(module_name)
    if not module:
        usage("No module '{}'".format(module_name))
    module.configure(configuration)
    module.main(argv[1:])

if __name__ == "__main__":
    main(sys.argv)

