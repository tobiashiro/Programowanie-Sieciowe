import socket, time, logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s, MAIN THREAD) %(message)s',)


class BroadcastServer:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.port = 0

    def create_connection(self, event):
        event.wait()
        self.port = input("Listening port (default - 7): ")
        if len(self.port) == 0:
            self.port = 7
        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.sock.settimeout(0.2)
            message = b"your very important message"
            while True:
                self.sock.sendto(message, ('<broadcast>', self.port))
                print("message sent!")
                time.sleep(1)
        except Exception as e:
            logging.debug("You put incorrect format. Error name: {}".format(e))

    def run(self, event):
        self.create_connection(event)
