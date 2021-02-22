import socket, logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s, MAIN THREAD) %(message)s',)


class BroadcastClient:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.port = 0

    def create_connection(self, event):
        self.port = input("Listening port (default - 7): ")
        if len(self.port) == 0:
            self.port = 7
        event.set()
        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.sock.bind(("", self.port))

            while True:
                data, addr = self.sock.recvfrom(1024)
                logging.debug("Client recive data: {} from {}".format(data, addr))
        except Exception as e:
            logging.debug("You put incorrect format. Error name: {}".format(e))

    def run(self, event):
        self.create_connection(event)
