import time
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

#Set up macros
def get_macros():
    macro_names={0: "Previous",1: "Play/Pause",2: "Next",3: "Rewind",4: "*",5: "Fast forward",6: "Vol+",7: "Vol-",8: "Mute"}
    return macro_names

def keypress(btn, cc, keyboard, write_text):
    if btn == 0:
        keyboard.send(Keycode.G)
        time.sleep(0.2)
    elif btn == 1:
        keyboard.send(Keycode.G)
        time.sleep(0.2)
    elif btn == 2:
        keyboard.send(Keycode.G)
        time.sleep(0.2)
    elif btn == 3:
        keyboard.send(Keycode.G)
        time.sleep(0.2)
    elif btn == 4:
        keyboard.send(Keycode.G)
        time.sleep(0.2)
    elif btn == 5:
        keyboard.send(Keycode.G)
        time.sleep(0.2)
    elif btn == 6:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.2)
    elif btn == 7:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.2)
    elif btn == 8:
        cc.send(ConsumerControlCode.MUTE)
        time.sleep(0.2)