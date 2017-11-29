def build_message(version, message_list):
    return "MSG {} {}".format(version, " ".join(message_list))

def decode_message(version, message_data):
    parts = message_data.split(" ")
    if parts[0] != "MSG":
        return "Bad message"
    if parts[1] != version:
        return "Bad version"
    else:
        return " ".join(parts[2:])

