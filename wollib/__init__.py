import socket

def wake(mac_hex: str):
    mac_bytes = bytes.fromhex(mac_hex.replace(":", ""))
    magic_packet = b"\xff" * 6 + (mac_bytes * 16)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(magic_packet, ("255.255.255.255", 9))
    sock.close()