# クイズ形式のif分の使い方

while True:
    print("第一問: AI（人工知能）が大量のデータから自動的に特徴を抽出し、学習する機械学習の一手法とは？")
    input_text = input("答えを入力:")

    if input_text in ("ディープラーニング", "深層学習"):
        print("正解")
        pass
    else:
        print("不正解")
        continue

    print("第二問: 複数のコンピュータからターゲットのサーバーに大量のアクセスを送りつけ、サービスを停止させるサイバー攻撃の名称は？")
    input_text = input("○○○○攻撃の○○○○を答えよ:")
    if input_text.lower == "ddos":
        print("正解:GAMEクリア")
        break
    else:
        print("不正解")
        continue

    