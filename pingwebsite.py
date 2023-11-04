# Python-project
import subprocess
import pyfiglet

text = pyfiglet.figlet_format("CraZy #RSM#")
print(text)
print("Enter an Ip")
i = input()
subprocess.call("ipconfig")
