import codecs
import socket


def wake_on_lan(ip: str, mac: str, port: int = 9):
    """Send magic Wake-on-LAN packet.
    Assumes the following input format:
      - ip: A valid IPv4 address, dot-separated like ###.###.###.###
      - mac: A valid MAC address, like XX:XX:XX:XX:XX:XX with hex values separated by :
    """

    # Define the payload
    # According to https://en.wikipedia.org/wiki/Wake-on-LAN, this should be
    #   6 bytes of 255 (0xFF) followed by 16 times the target MAC address
    mac = mac.replace(':', '')
    payload = codecs.decode(('FF' * 6) + (mac * 16), 'hex')

    # Set up socket
    # Parameters based on https://apple.stackexchange.com/a/287814
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send & verify
    bytes_sent = s.sendto(payload, (ip, port))
    if bytes_sent != 102:
        return False

    return True
