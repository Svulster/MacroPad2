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
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        time.sleep(0.2)
    elif btn == 1:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.2)
    elif btn == 2:
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.2)
    elif btn == 3:
        cc.send(ConsumerControlCode.REWIND)
        time.sleep(0.2)
    elif btn == 4:
        keyboard.send(Keycode.ALT, Keycode.SHIFT, Keycode.B)
        time.sleep(0.2)
    elif btn == 5:
        cc.send(ConsumerControlCode.FAST_FORWARD)
        time.sleep(0.2)
    elif btn == 6:
        keyboard.send(Keycode.CONTROL, Keycode.UP_ARROW)
        print("Volume up")
        time.sleep(0.2)
    elif btn == 7:
        keyboard.send(Keycode.CONTROL, Keycode.DOWN_ARROW)
        print("Volume down")
        time.sleep(0.2)
    elif btn == 8:
        cc.send(ConsumerControlCode.MUTE)
        time.sleep(0.2)
