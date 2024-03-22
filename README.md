# Yeelight mute indicator
![image](https://raw.githubusercontent.com/Moringar/YeelightNotifications/main/yeemute.png?token=GHSAT0AAAAAACODXPV3TMVUFSDH4YE4S3UAZP6C3CQ)
## Flashes red when you are mute, green when you are not. no doubts.

I needed a clear indicator to know when i'm mute on voice channels, so i did this.<br>
No discord bot is required : a controller and a lightbulb is enough. <br>
The yeelight python library is needed : [url](https://gitlab.com/stavros/python-yeelight)


### SETUP

Provide the local ip addresses of your bulbs:
```sh
bulbRight = Bulb("192.168.1.155")
bulbLeft = Bulb("192.168.1.61")
```
Select you HID device
```sh
controller.open(0x1b4f, 0x9206)
```

select the button to use to trigger notifications
```sh
if inputReport[3] == 8:
```


🛠️ This script can be easily modified to suit more bulbs and more notifications types.<br>
Ideas :
- Trigger for windows notifications
- connection to a discord bot

#### 🟢 This script is light an use minimal ressources from CPU / RAM.

## Installation
#### manual start:
double click the script. 👌

#### Auto start:
To start the script at windows startup, put the python script in:
```sh
C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```
It's working 👍
