# Fetch Password (Windows)
_____________________________________________________________________________________
This piece of code can show you the password of connected or known wifi-network
and allow you to generate QR Code for password or to copy password to your clipboard
_____________________________________________________________________________________
## Behind the Hood
Behind the hood, this program usage the Command-Line system of windows.
You can easily view password of your desired network(Known Host) using follow command
in Command Prompt or Powershell
1. First o display names of all the known network use
````
netsh wlan show profile
````
2. Now to view the password, just copy the name of your desired network from list and type in
following command.
````
netsh wlan show profile [PASTE NETWORK NAME] key=clear
````
3. Now under security, there is your password as Key Content