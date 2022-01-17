from urllib import request
import main
from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html",host_name=main.getHost(),wifi_info = main.WIFI_INFO)


@app.route("/<string:wifi_name>",methods=['POST'])
def delete_wifi(wifi_name):
    return render_template("index.html",host_name=main.getHost(),wifi_info = main.WIFI_INFO,deleted_wifi=wifi_name)


if __name__ == "__main__":
    app.run(debug=True,port=6060)
    

















