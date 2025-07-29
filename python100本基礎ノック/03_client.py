### 03_client.py
### 悪用厳禁です。socket通信の側のクライアント側のコードです。

import subprocess
import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(("127.0.0.1", 9000))
    print("接続完了")

    while True:
        try:
            cmd = input("SHELL>>:").strip()
            if not cmd:
                continue
            if cmd.lower() == "exit":
                break
            c.sendall(cmd.encode())

            output = c.recv(4096).decode()
            print(output)
        except Exception as e:
            print(f"エラー: {str(e)}")
            break
