
"""

postgre ダウンロード
https://www.postgresql.org/download/windows/

PostgreSQLをWindowsにインストールするには
https://qiita.com/tom-sato/items/037b8f8cb4b326710f71

【入門】PostgreSQLをインストールして簡単なデータベースを作ってみよう
https://houmatsu.kinova.jp/tech-blog/blog/postgresql-installation-guide/

"""


import polars as pl
import psycopg2
import json

# PostgreSQL接続情報の設定
user="postgres"
password="p@ssword"
host="localhost"
port=5432
dbname="mydb"

def search_by_id(id: str):
    """
    指定されたIDに基づいてtable1からレコードを検索し、JSON形式で返す関数

    Args:
        id (str): 検索対象のID

    Returns:
        str: 検索結果をJSON文字列で返す
    """
    # データベースに接続
    conn = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        dbname=dbname
    )
    # SQLクエリを作成
    query = f"SELECT id, name, age FROM table1 WHERE id = '{id}'"
    # Polarsを使ってクエリ結果をDataFrameとして取得
    df = pl.read_database(query, conn)
    # DataFrameを辞書のリストに変換
    result = df.to_dicts()
    # 接続を閉じる
    conn.close()
    # 結果をJSON文字列に変換して返す
    return json.dumps(result, ensure_ascii=False)

def insert_data(id: str, name: str, age: int):
    """
    table1に新しいレコードを挿入する関数

    Args:
        id (str): 挿入するID
        name (str): 挿入する名前
        age (int): 挿入する年齢
    """
    import psycopg2
    try:
        # データベースに接続
        conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            dbname=dbname
        )
        # カーソルを作成
        cur = conn.cursor()
        # INSERT文を実行
        cur.execute("INSERT INTO table1 (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
        # 変更をコミット
        conn.commit()
        # カーソルと接続を閉じる
        cur.close()
        conn.close()
    except Exception as e:
        # エラー発生時はエラーメッセージを表示
        print(f"Error inserting data: {e}")


def update_data(id: str, name: str, age: int):
    """
    指定されたIDのレコードのnameとageを更新する関数

    Args:
        id (str): 更新対象のID
        name (str): 更新する名前
        age (int): 更新する年齢
    """
    try:
        # データベースに接続
        conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            dbname=dbname
        )
        # カーソルを作成
        cur = conn.cursor()
        # UPDATE文を実行
        cur.execute("UPDATE table1 SET name = %s, age = %s WHERE id = %s", (name, age, id))
        # 変更をコミット
        conn.commit()
        # カーソルと接続を閉じる
        cur.close()
        conn.close()
    except Exception as e:
        # エラー発生時はエラーメッセージを表示
        print(f"Error updating data: {e}")

if __name__ == "__main__":
    # テスト用のデータ
    test_id ='A07'
    test_name = '鈴木一郎'
    test_age = 30

    # データ挿入関数を呼び出し
    insert_data(test_id, test_name, test_age)

    # 挿入したデータをIDで検索し、結果を取得
    result_json = search_by_id(test_id)
    
    # 検索結果を表示
    print("Before update:", result_json)

    # update_data関数を呼び出し
    update_data(test_id, "田中太郎", 35)

    # 更新後のデータをIDで検索し、結果を取得
    updated_result_json = search_by_id(test_id)

    # 更新結果を表示
    print("After update:", updated_result_json)
