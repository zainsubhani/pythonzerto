from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world(username):
    return render_template('.index.html')

@app.route("/<username>")