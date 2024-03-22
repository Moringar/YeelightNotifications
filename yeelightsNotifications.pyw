from yeelight import Bulb
import hid
import time

#note: color mode: 1 = COLOR, 2 = TEMPERATURE

#Lightbulbs IP
bulbRight = Bulb("192.168.1.155")
bulbLeft = Bulb("192.168.1.61")
isMute = 0
# savedStateB = bulbB.get_properties()

# Gets and save color settings before notification.
def savebulbState():
    saveStateBulbRight = bulbRight.get_properties()
    saveStateBulbLeft = bulbLeft.get_properties()
    return [saveStateBulbRight, saveStateBulbLeft]

# Sets lightbulbs colors according to saved states OR manual settings
def setBulbColor(colorMode1, brightness1, hue1, saturation1, colorTemperature1,colorMode2, brightness2, hue2, saturation2, colorTemperature2):
    if colorMode1 == 1:
        bulbRight.set_hsv(int(hue1), int(saturation1), int(brightness1))
    elif colorMode1 == 2:
        bulbRight.set_color_temp(int(colorTemperature1))
        bulbRight.set_brightness(brightness1)
    if colorMode2 == 1:
        bulbLeft.set_hsv(int(hue2), int(saturation2), int(brightness2))
    elif colorMode2 == 2:
        bulbLeft.set_color_temp(int(colorTemperature2))
        bulbLeft.set_brightness(brightness2)

# Profile of the mute button
controller = hid.device()
controller.open(0x1b4f, 0x9206)
controller.set_nonblocking(True)

while True:
    # time.sleep prevents this script to overwhelm the CPU
    time.sleep(0.5)

    #Reads inputs from the controller/buttonBox ect
    inputReport = controller.read(64)
    if inputReport:

        
        
        #If the selected button is pressed
        if inputReport[3] == 8:

            #Save bulb state when button pressed before notification.
            savedState= savebulbState()
            print(savedState)
            
            #If not mute : flash red notification and reset to saved state.
            if isMute == 0:
                setBulbColor(1,100,359,100,0,1,100,359,100,0)
                time.sleep(0.5)
                setBulbColor(int(savedState[0]['color_mode']), int(savedState[0]['bright']), int(savedState[0]['hue']), int(savedState[0]['sat']), int(savedState[0]['ct']),int(savedState[1]['color_mode']), int(savedState[1]['current_brightness']), int(savedState[1]['hue']), int(savedState[1]['sat']), int(savedState[1]['ct']))
                isMute = 1
                print("mute")

            #If mute : flash green notification and reset to saved state.
            elif isMute == 1:
                setBulbColor(1,100,123,100,0,1,100,123,100,0)
                time.sleep(0.5)
                setBulbColor(int(savedState[0]['color_mode']), int(savedState[0]['bright']), int(savedState[0]['hue']), int(savedState[0]['sat']), int(savedState[0]['ct']),int(savedState[1]['color_mode']), int(savedState[1]['current_brightness']), int(savedState[1]['hue']), int(savedState[1]['sat']), int(savedState[1]['ct']))
                isMute = 0
                print("unmute")