# 특정한 URI를 요청하면 JSON 형식으로 데이터를 반환하도록 만듦
# 즉, 웹주소(URI) 요청에 대한 응답(Response)를 JSON 형식으로 작성
# Flask에서는 dict(사전) 데이터를 응답 데이터로 만들고, 이를 jsonify() 메서드를 활용해서 JSON 응답 데이터로 만들수 있음

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/json_test')
def hello_json():
    data = {'name':'jinkyukim', 'address':'seocho'}
    return jsonify(data)

@app.route('/server_info')
def server_json():
    data = {'server_name':'127.0.0.1','server_port':'8080'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port="8080")
