from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World~!!!!"

@app.route('/about')
def about():
    return "The About Page"

@app.route('/blog')
def blog():
    return "This is the blog"

@app.route('/doremi')
def doremi():
    import doremi


# @app.route('blog/<blog_id>')
# def blogpost(blog_id):
#     return "This iis blog post number" + str(blog_id)

if __name__ == "__main__":
    app.run()
