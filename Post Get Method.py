from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return "welcome %s" % name

@app.route('/')
def hi():
    return "<h1>The Guide for Flask Professional</h1>"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form['myName']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('myName')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(host="127.0.0.5", port="8080")
