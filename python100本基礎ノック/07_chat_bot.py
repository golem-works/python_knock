#簡単なチャットボットresに登録した辞書を返します。

import re


res = {
    "こんにちは":"こんにちは、アシスタントBOTです。",
    "Hello":"こんにちは、アシスタントBOTです。",
    "テスト":"応答します"
}

state = False
while True:
    user = input("ご用件はなんでしょうか？:").strip()
    if user == "exit":
        print("baybay!")
        break
    
    for key, word in res.items():
        if key in user:
            print(word)
            state = True
            break
        
    if not state:
        print("すみません。よくわかりません。")
        continue
    