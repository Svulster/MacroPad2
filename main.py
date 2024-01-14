import rotaryio, digitalio, board, usb_hid
import time
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

from windows_mode import keypress as windows_keypress
from windows_mode import get_macros as get_windows_macros
from music_mode import keypress as music_keypress
from music_mode import get_macros as get_music_macros
from obsidian_mode import keypress as obsidian_keypress
from obsidian_mode import get_macros as get_obsidian_macros
from fusion_mode import keypress as fusion_keypress
from fusion_mode import get_macros as get_fusion_macros

#Set up buttons
buttons = [board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7]
key = [digitalio.DigitalInOut(pin_name) for pin_name in buttons]
for x in range(0,len(buttons)):
    key[x].direction = digitalio.Direction.INPUT
    key[x].pull = digitalio.Pull.DOWN

modeChangeButton = digitalio.DigitalInOut(board.GP15)
modeChangeButton.direction = digitalio.Direction.INPUT
modeChangeButton.pull = digitalio.Pull.DOWN

encButton = digitalio.DigitalInOut(board.GP20)
encButton.direction = digitalio.Direction.INPUT
encButton.pull = digitalio.Pull.UP

#Set up encoder
encoder = rotaryio.IncrementalEncoder(board.GP18, board.GP19)
button_state = None
last_position = encoder.position

# Set up Consumer Control - Control Codes can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/consumer_control_code.html#ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)
# Set up a keyboard device. - Keycode can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
keyboard = Keyboard(usb_hid.devices)
# Set up keyboard to write strings from macro
write_text = KeyboardLayoutUS(keyboard)

#Set up modes
mode_names = {1 : 'Windows', 2 : 'Spotify', 3 : "Obsidian", 4 : "Fusion 360"}
mode = 1 

def send(btn):
    if mode == 1:
        windows_keypress(btn, cc, keyboard, write_text)
    elif mode == 2:
        music_keypress(btn, cc, keyboard, write_text)
    elif mode == 3:
        obsidian_keypress(btn, cc, keyboard, write_text)
    elif mode == 4:
        fusion_keypress(btn, cc, keyboard, write_text)

while True:
    #Check change mode button
    if modeChangeButton.value:
        mode = mode + 1
        if mode > len(mode_names):
            mode = 1
        print(mode_names[mode])
        time.sleep(1)
    
    #Check encoder
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            send(6)
    elif position_change < 0:
        for _ in range(-position_change):
            send(7)
    last_position = current_position
    
    #Check encoder button
    if not encButton.value and button_state is None:
        button_state = "pressed"
    if encButton.value and button_state == "pressed":
        send(8)
        button_state = None
    
    #Check macro buttons
    if key[0].value:
        send(0)
        time.sleep(0.2)
         
    if key[1].value:
        send(1)
        time.sleep(0.2)
        
    if key[2].value:
        send(2)
        time.sleep(0.2)
    
    if key[3].value:
        send(3)
        time.sleep(0.2)
    
    if key[4].value:
        send(4)
        time.sleep(0.3)
        
    if key[5].value:
        send(5)
        time.sleep(0.3)