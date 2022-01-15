import main
from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html",host_name=main.getHost())

if __name__ == "__main__":
    app.run(debug=True,port=6060)

















