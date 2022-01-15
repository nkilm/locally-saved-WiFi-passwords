import subprocess
import re

def getHost():
    host_name = subprocess.run('hostname',capture_output=True,shell=True).stdout.decode()
    host_name = host_name.replace("\n","").replace("\r","")
    return host_name

def getWifiNames():
    cmd_output = subprocess.run(
        'netsh wlan show profiles', shell=True, capture_output=True)
    output = cmd_output.stdout.decode()
    saved_wifi_names = re.findall("All User Profile     : (.*)", output)
    # starts with 'All User Profile     :' (.*) means anything of length>=0
    if(len(saved_wifi_names) == 0):
        return "No saved WiFi"
    result = []
    for wifi_name in saved_wifi_names:
        result.append(wifi_name.replace("\r", ""))
    return result


def getWiFInfo(wifi_name):
    # cmd_output = subprocess.run(['netsh','wlan','show','profiles',wifi_name,'key','=','clear'],capture_output=True)
    cmd_output = subprocess.run(
        f"netsh wlan show profiles \"{wifi_name}\" key=clear", shell=True, stdout=subprocess.PIPE)
    formatted_output = cmd_output.stdout.decode()

    security_key = re.search(
        "Security key           : (.*)", formatted_output).group(0).replace("\r", "")
    # split and store only security status
    security_key = security_key.split(": ")[1]

    # proceed only if security key = Present
    if(security_key == "Present"):
        password = re.search("Key Content            : (.*)", formatted_output)
        password = password.group(0).replace("\r", "").split(": ")[
            1]  # split and store only password
        print(password)
    else:
        print("--None--")



if __name__ == "__main__":
    # Testing the functions defined

    # print(getWifiNames())
    getWiFInfo("OnePlus_Nik")
    getWiFInfo("Hita's Galaxy S10 Lite")
    getWiFInfo("PESU-Element Block")

