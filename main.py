
import subprocess
import re
from unittest import result

cmd_output = subprocess.run('netsh wlan show profiles',shell=True,capture_output=True)

output = cmd_output.stdout.decode()

saved_wifi_names = re.findall("All User Profile     :(.*)",output)
# starts with 'All User Profile     :' (.*) means anything of length>=0

result = [];

for wifi_name in saved_wifi_names:
    result.append(wifi_name.replace(" ","").replace("\r",""))


if __name__=="__main__":
    # print(output)
    print(saved_wifi_names)
    print(result)









