from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>파이썬을 이용한 머신러닝, 딥러닝 실전 개발 입문</h1>"

@app.route("/hello")
def hello_flask():
    return "<h2>안녕~~~ Flask 만나서 반가워~</h2>"

@app.route("/first/<username>")
def hello_first(username):
    return "<h3>점점 작아지는 글씨에 멘붕이 옴</h3>" + username + "!</h3>"

@app.route("/profile/<username>")
def get_profiile(username):
    return "profile: " + username

@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id

@app.route("/second/<int:messageid>")
def get_first(messageid):
    return "<h1>%d</h1>" % (messageid + 5)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
