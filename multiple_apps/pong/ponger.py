import sys
import shared.util


def ponger(settings, log_file):
    with open(log_file, "w") as fp:
        fp.write("Version: {}\n".format(settings["version"]))
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.rstrip()
            fp.write("Received: {}\n".format(line))
            reply = shared.util.decode_message(settings["version"], line)
            print(reply)
            fp.write("Replied: {}\n".format(reply))

if __name__ == "__main__":
    # Any testing here
    pass

