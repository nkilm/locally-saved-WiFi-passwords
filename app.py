import json
import main
from flask import Flask,render_template


WIFI_INFO = []

for wifi in main.getWifiNames():
    security_type,key = main.getWiFInfo(wifi)
    WIFI_INFO.append([wifi,security_type,key])


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html",host_name=main.getHost(),wifi_info = WIFI_INFO)


@app.route("/<string:wifi_name>",methods=['POST'])
def delete_wifi(wifi_name):
    wifi_name = json.loads(wifi_name) # json string to dict 

    msg,res_code = main.deleteWifi(wifi_name['name'])
    if(res_code==0):
        return render_template("index.html",host_name=main.getHost(),wifi_info = WIFI_INFO)
    return render_template("error.html",error_message=msg,error_code=res_code,wifi_name = wifi_name['name'])


if __name__ == "__main__":
    app.run(debug=True,port=6060)
    

















