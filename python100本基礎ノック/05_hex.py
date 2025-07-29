### １６進数からの文字変換

hex_string = "70 79 74 68 6f 6e e5 ad a6 e7 bf 92"

# スペースを除去してからバイト変換
cleaned = hex_string.replace(" ", "")
byte_data = bytes.fromhex(cleaned)
result = byte_data.decode("utf-8")

print(result)  # python学習
