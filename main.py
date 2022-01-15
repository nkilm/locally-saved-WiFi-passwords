
import subprocess

cmd_output = subprocess.run('netsh wlan show profiles',shell=True,capture_output=True)

output = cmd_output.stdout.decode()


if __name__=="__main__":
    print(output)










