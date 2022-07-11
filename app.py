from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/join')
def join():
    return render_template("join.html")

@app.route('/review')
def review():
    return render_template("review.html")




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)