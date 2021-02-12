import socket


class Client:

    def __init__(self, sock=None):
        self.host = None
        self.port = None
        print("start client")
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self):
        try:
            self.sock.connect((self.host, int(self.port)))
            print("Server connected")
        except Exception as e:
            print("Connection problem. Error name {}".format(e))
            exit(1)

    def send(self):
        while True:
            msg = str(input("Message to send: "))
            if msg == "quit":
                self.sock.close()
                break
            else:
                self.sock.send(msg.encode("utf-8"))
                check = self.sock.recv(1024).decode("utf-8")
                if msg == check:
                    print("mesage sent: "+check)
                else:
                    print("Something went wrong")
                print("Message sent. If you want to exit type 'quit'.")
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, int(self.port)))

    def input_data(self):
        self.host = str(input("TCP server IP or domain name (default: localhost): "))
        if len(self.host) == 0:
            self.host = "localhost"
        self.port = input("Listening port (default - 7): ")
        if len(self.port) == 0:
            self.port = 7
        elif self.port.isnumeric():
            self.port = int(self.port)
        else:
            raise Exception("You put incorrect format")


client = Client()
client.input_data()
client.connect()
client.send()


