import lib.util


def hello(settings, verbose):
    message = settings["message"]
    if verbose:
        print("Found message setting: {}".format(message))
    print(lib.util.routine(message))

if __name__ == "__main__":
    # Any testing here
    hello({"message": "Another message"}, False)

