from os import startfile
import subprocess, pyqrcode, pyperclip

def createQrCode(data):
    qr = pyqrcode.create(data)
    qr.png("wifi_password_qr_code.png", scale=8)
output = subprocess.check_output('netsh wlan show profiles').decode()

output = output.split("User profiles")[1].replace("    All User Profile     :", "").replace("-------------", "")
namelist = list(set(output.split("\r\n")))
count = 1
print("""Menu
    Choose the Wi-Fi SSIS
    to view Password
""")
for names in namelist:
    if names == '':
        namelist.remove(names)
    else:
        print(f"{count})", names)
        count += 1
index = input("Enter Index: ")
wifiname = namelist[int(index)].replace(' ', '', 1)
newOutput = subprocess.check_output("""netsh wlan show profiles "{}" key=clear""".format(wifiname)).decode()
splitedOut = newOutput.split("Security settings")[1].split("Cost settings")[0].replace("-----------------", "").split('\r\n')
for password in splitedOut:
    if "Key Content" in password:
        extracted_password = password.replace("    Key Content            : ", "")
        print("Password\n", extracted_password)
command = int(input("""Choose Options
    1. Copy to clipboard
    2. Show QR Code
    99. Exit
"""))
if command == 1:
    pyperclip.copy(extracted_password)
    print("Copied to clipboard")
elif command == 2:
    createQrCode(extracted_password)
    startfile("wifi_password_qr_code.png")
elif command == 99:
    exit()