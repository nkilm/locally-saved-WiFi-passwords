
import subprocess
import re

cmd_output = subprocess.run('netsh wlan show profiles',shell=True,capture_output=True)

output = cmd_output.stdout.decode()

saved_wifi_names = re.findall("All User Profile     :(.*)",output)
# starts with 'All User Profile     :' (.*) means anything of length>=0


if __name__=="__main__":
    # print(output)
    print(saved_wifi_names)









