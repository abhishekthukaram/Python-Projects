import binascii
import socket

def convert2hex(input_str):
    hex_output = binascii.hexlify(socket.inet_aton(input_str))
    return hex_output


print(convert2hex('20.20.20.104'))
