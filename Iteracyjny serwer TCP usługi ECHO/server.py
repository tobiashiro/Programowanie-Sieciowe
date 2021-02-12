import socket
import sys


class Server:

    def __init__(self, sock=None, host=None):
        self.port = None
        self.host = None
        print("start server")
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self):
        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen(5)
            print("Adress binded")
        except Exception as e:
            print("Connection problem. Error name: {}".format(e))
            exit(1)

    def rcv(self):
        while True:
            try:
                clientsocket, address = self.sock.accept()
                print("Connection from {} has been established".format(address))
                full_msg = ""
                msg = clientsocket.recv(1024)
                full_msg = msg.decode("utf-8")
                clientsocket.send(full_msg.encode("utf-8"))
                print(full_msg)
                clientsocket.close()
            except Exception as e:
                print("Recive data probmem. Error name: {}".format(e))
                clientsocket.close()
                break
                exit(1)

    def input_port(self):
        try:
            self.port = input("Listening port (default - 7): ")
            if len(self.port) == 0:
                self.port = 7
            elif self.port.isnumeric():
                self.port = int(self.port)
            else:
                raise Exception("You put incorrect format")
            self.host = input("Listening host (default - localhost): ")
            if len(self.host) == 0:
                self.host = "127.0.0.1"
            else:
                try:
                    socket.inet_aton(self.host)
                except Exception as e:
                    print("host parameter is incorrect. Error name: {}".format(e))
                    sys.exit(1)
        except Exception as e:
            print("input parameters are incorrect. Error name: {}".format(e))



server = Server()
server.input_port()
server.connect()
server.rcv()

