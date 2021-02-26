from flask import Flask, render_template, url_for, request
from start import parsing


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/parse", methods=['POST'])
def parse():
    login = request.form['login']
    password = request.form['password']
    keywords = request.form['keywords']
    table = parsing(login, password, keywords)
    return render_template("table.html", table=table, table_len=len(table))


if __name__ == '__main__':
    app.run(debug=True)