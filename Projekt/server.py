import socket
import sys, threading, struct, time, temporenc, easygui
from datetime import datetime


class Server:

    def __init__(self, sock=None, host=None):
        self.port = None
        self.host = None
        self.eventStop = None
        self.amount_of_connections = 0
        self.thread_connections = []
        print("start server")
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, eventStart):
        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen(5)
            print("Adress binded")
            eventStart.set()
        except Exception as e:
            print("Connection problem. Error name: {}".format(e))
            exit(1)

    def thread_connection(self, clientsocket):
        try:
            server_time = time.time_ns() / 1000000
            clientsocket.send(bytes(str(server_time), 'utf-8'))
        except Exception as e:
            print("Recive data probmem from method thred_connection(). Error name: {}".format(e))
            clientsocket.close()
            exit(1)
        clientsocket.close()

    def rcv(self):
        while True:
            if self.eventStop.isSet():
                print("Server close connection. Flag is set")
                self.sock.close()
                exit(1)
                break
            try:
                clientsocket, address = self.sock.accept()
                print("Server: Connection from {} has been established".format(address))
                th = threading.Thread(target=self.thread_connection, args=(clientsocket, ))
                self.thread_connections.append(th)
                th.start()
            except Exception as e:
                print("Recive data probmem from rcv() method. Error name: {}".format(e))
                clientsocket.close()
                break
                exit(1)

    def input_port(self):
        msg = "Enter server information: "
        title = "Server"
        fieldNames = ["Port (empty - default: 7)", "Host(empty - default: localhost)"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg, title, fieldNames)

        while True:
                problems = False
                self.port = fieldValues[0]
                if fieldValues[0] == '':
                    self.port = 7
                else:
                    try:
                        tmp_port = int(fieldValues[0])
                    except Exception as e:
                        problems = True

                self.host = fieldValues[1]
                if fieldValues[1] == '':
                    self.host = "127.0.0.1"

                try:
                    socket.inet_aton(self.host)
                except Exception as e:
                    problems = True

                if problems == True:
                    errmsg = "You Put iccorrect format. Try again"
                    fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
                else:
                    break

    def run(self, event, eventStop):
        self.eventStop = eventStop
        self.input_port()
        self.connect(event)
        self.rcv()

