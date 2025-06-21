#ただ単純にファイルをwindowsで開く

import sys
import os

def file_nock(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        files = f.read()
        print(files)
        
if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except Exception as e:
        print("file名を指定してください。")
        
    file_nock(file_name)
    os.startfile(file_name)
    
 