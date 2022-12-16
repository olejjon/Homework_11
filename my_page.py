from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template("my_page.html")

app.run(port=5000)