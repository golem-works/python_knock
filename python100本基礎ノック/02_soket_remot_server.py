# TCPserverを自作   遠隔で操作できるsocketのサーバ側

import sys
import os
import socket
import subprocess

IP = sys.argv[1]
PORT = int(sys.argv[2])
num = int(sys.argv[3])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen(num)
    
    conn, addr = s.accept()
    conn.sendall(f"接続待機 IP:{IP} PORT:{PORT} 受け入れ数:{num}".encode())
    
    
    while True:
        try:
            cmd = conn.recv(1024).decode().strip()
            if cmd in ("exit","quit"):
                print(f"リモートを終了:{cmd}")
                break
                
            if cmd.startswith("cd "):
                try:
                    os.chdir(cmd[3:].strip())
                    conn.sendall(f'{cmd}:{os.getcwd()}'.encode())
                except Exception as e:
                    conn.sendall(f'コマンドエラー:{e}'.encode())
                continue
                
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                output = e.output
            conn.sendall(output)
                
        except Exception as e:
            conn.sendall(f"error:{e}".encode())
                    