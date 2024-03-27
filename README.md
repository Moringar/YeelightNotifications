# Yeelight mute indicator
![image](https://raw.githubusercontent.com/Moringar/YeelightNotifications/main/yeemute.png?token=GHSAT0AAAAAACODXPV2BXNBTVBDFBGRVD7AZP6DDXQ)
## Flashes red when you are mute, green when you are not. no doubts.

I needed a clear indicator to know when i'm mute on voice channels, so i did this.<br>
No discord bot is required : a controller and a lightbulb is enough. <br>
The yeelight python library is needed : [here](https://gitlab.com/stavros/python-yeelight)


### SETUP


Provide the local ip addresses of your bulbs, you can find it in you yeelight app and un your router interface:
```sh
bulbRight = Bulb("192.168.1.155")
bulbLeft = Bulb("192.168.1.61")
```

the extension .pyw which will cause the script to be executed by pythonw.exe, in the background. So, to see returned values avout yours devices and inputs, set it to .py.



Select you HID device:
This will enumerate all you devices : Keyboard/mouse/controller/arduino ect.
```sh
devices = hid.enumerate()
```
Choose the on you need, and format the following line like : controller.open(VENDOR ID, PRODUCT ID)
```sh
controller.open(0x1b4f, 0x9206)
```

Then, "push/pull/smash" the "button/trigger/sensor" of your device, see what data is affected, then pinpoint the data in the array that will trigger your event:
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
