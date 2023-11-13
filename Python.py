import tkinter as tk
from pynput import keyboard
import time

# Making a little GUI for buttons
class KeystrokeRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Keystroke Recorder")
        self.record_button = tk.Button(self.master, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=10)
        self.stop_record_button = tk.Button(self.master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_record_button.pack(pady=10)
        self.loop_button = tk.Button(self.master, text="Start Looping", command=self.start_loop, state=tk.DISABLED)
        self.loop_button.pack(pady=10)
        self.keystrokes = []
#def what the start recording button does
    def start_recording(self):
        self.record_button["state"] = tk.DISABLED
        self.stop_record_button["state"] = tk.NORMAL
        self.loop_button["state"] = tk.DISABLED
        self.keystrokes = []  # Clear previous keystrokes
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()
#def what the stop recording button does
    def stop_recording(self):
        self.record_button["state"] = tk.NORMAL
        self.stop_record_button["state"] = tk.DISABLED
        self.loop_button["state"] = tk.NORMAL
        if hasattr(self, 'listener'):
            self.listener.stop()
#making it so that You can press any type of type
    def on_key_press(self, key):
        try:
            self.keystrokes.append(key.char)
        except AttributeError:
            self.keystrokes.append(str(key))
#def what the start loop button does
    def start_loop(self):
        self.record_button["state"] = tk.DISABLED
        self.stop_record_button["state"] = tk.DISABLED
        self.loop_button["state"] = tk.DISABLED

# Adding a 5 sec delay so that you have time to change screens to what you are doing
        delay_seconds = 5
        self.master.after(int(delay_seconds * 1000), self.perform_loop)
#The takes the keys we inputed before and loops them
    def perform_loop(self):
        controller = keyboard.Controller()
        for key in self.keystrokes:
            if key.startswith("Key."):
                key_name = key.split(".")[1].lower()
                controller.press(eval(f"keyboard.Key.{key_name}"))
                controller.release(eval(f"keyboard.Key.{key_name}"))
            else:
                controller.press(key)
                controller.release(key)
# Delay so that it does not trip itself up
            time.sleep(0.1) 
        self.record_button["state"] = tk.NORMAL
        self.stop_record_button["state"] = tk.DISABLED
        self.loop_button["state"] = tk.NORMAL
# Creating the window that opens for the buttons
if __name__ == "__main__":
    root = tk.Tk()
    app = KeystrokeRecorderApp(root)
    root.mainloop()
