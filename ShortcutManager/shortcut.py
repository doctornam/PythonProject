'''
pip install pynput, pypiwin32
'''

from pynput.keyboard import Key, Listener, KeyCode
import win32api

MYKEYS = [
    {"function1": {Key.shift, KeyCode(char='a')}},
    {"function2": {Key.ctrl_l, Key.alt_l, KeyCode(char='n')}},
]

current_keys = set()

def function1():
    print("함수1")
    win32api.WinExec("calc.exe")

def function2():
    print("함수2")
    win32api.WinExec("notepad.exe")

def key_pressed(key):
    print("Press {}".format(key))
    for data in MYKEYS:
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]
        if key in KEYS:
            current_keys.add(key)
            if all(k in current_keys for k in KEYS):
                function = eval(FUNCTION)
                function()

def key_released(key):
    print("Release {}".format(key))
    for data in MYKEYS:
        KEYS = list(data.values())[0]
        if key in KEYS:
            current_keys.remove(key)
    if key == Key.esc:
        return False

with Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()