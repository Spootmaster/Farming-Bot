from pynput import keyboard
import pyautogui
import time

#List of Keystrokes
keystrokes = []

#Function to record key presses
def on_key_press(key):
    try:
        keystrokes.append(key.char)
    except AttributeError:
        #Handle special keys
        keystrokes.append(str(key))

#Keystrokes Recorder
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()

#Print the recorded keystrokes
print("Recorded Keystrokes:", keystrokes)

#Replay Keystrokes
def play_back_keystrokes(keystrokes):
    with keyboard.Controller() as controller:
        for key in keystrokes:
            controller.press(key)
            controller.release(key)
            time.sleep(0.1)

# Play back the recorded keystrokes
play_back_keystrokes(keystrokes)
