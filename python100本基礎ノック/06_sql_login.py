### mysqlに接続してログイン処理を行うコード
### pip install mysql-connector-python でインストールが必要

import mysql.connector

# MySQLに接続
conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'localuser',
    password = '1111',
    database = 'users'
)

cursor = conn.cursor()

# ログイン関数
table_name = 'login'

def login(name, password):
    query = f"SELECT * FROM {table_name} WHERE name = %s AND password = %s"
    cursor.execute(query, (name, password))
    result = cursor.fetchone()
    if result:
        print("ログイン成功")
    else:
        print("ログイン失敗。ユーザー名とパスワードを確認してください。")

# ユーザー入力
username = input("user_name: ")
password = input("password: ")

# ログイン処理呼び出し
login(username, password)

# 接続終了
cursor.close()
conn.close()
