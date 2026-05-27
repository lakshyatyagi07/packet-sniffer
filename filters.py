def should_filter(protocol_name, args):

    if args.tcp and protocol_name != "TCP":
        return True

    if args.udp and protocol_name != "UDP":
        return True

    return False