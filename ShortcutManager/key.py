from pynput.keyboard import Key, Listener, KeyCode

MYKEYS = [
    {Key.shift, KeyCode(char='a')},
    {Key.ctrl_l, Key.alt_l, KeyCode(char='n')},
]

current_keys = set()

def run():
    print("RUN")

def key_pressed(key):
    print("Press {}".format(key))

    if any([key in KEY for KEY in MYKEYS]):
        current_keys.add(key)

        if any(all(k in current_keys for k in KEY) for KEY in MYKEYS):
            run()

    # for KEY in MYKEYS:
    #     if key in KEY:
    #         print("포함된 키 {} {}".format(key, current_keys))
    #         current_keys.add(key)
    #         check = True
    #         for k in KEY:
    #             if k not in current_keys:
    #                 check = False
    #                 break
    #         if check:
    #             run()


def key_released(key):
    print("Release {}".format(key))

    if any([key in KEY for KEY in MYKEYS]):
        current_keys.remove(key)

    # for KEY in MYKEYS:
    #     if key in KEY and key in current_keys:
    #         current_keys.remove(key)

    if key == Key.esc:
        return False

with Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()