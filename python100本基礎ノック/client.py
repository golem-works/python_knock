import os
import subprocess
import socket

IP = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP,PORT))
    
    while True:
            cmd = input("shell >>").strip()
            if cmd in ('exit' 'quit'):
                s.sendall(cmd.encode())
                break
            s.sendall(cmd.encode())
            result=s.recv(4096).decode()
            print(result)
            