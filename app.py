from flask import Flask

# Flaskインスタンスの生成
app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    ルートディレクトリにアクセスした際の処理を行う。

    Returns:
        str: ブラウザに表示する文字列
    """
    # 完了率の計算例（ルールに基づき $a / b \cdot 100$ の形式を意識）
    # 実際のToDo実装時にはここでDBから値を取得する
    return "Hello, World! ToDoアプリ開発開始だ！"

if __name__ == '__main__':
    # 開発用サーバーの起動
    app.run(debug=True)
