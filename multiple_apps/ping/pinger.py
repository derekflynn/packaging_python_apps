import sys
import ping.main
import shared.util


def pinger(settings, message_list, verbose):
    if verbose:
        sys.stderr.write("Version: {}\n".format(settings["version"]))
    message = shared.util.build_message(settings["version"], message_list)
    if verbose:
        sys.stderr.write("Message to send: {}\n".format(message))
    print(message)

if __name__ == "__main__":
    # Any testing here
    pass
