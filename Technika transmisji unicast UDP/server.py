import socket, logging, threading

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class Server:

    def __init__(self):
        self.connections = 0

    def start_server(self):
        logging.debug("Start server")
        UDP_IP = "127.0.0.1"
        UDP_PORT = 7
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.bind((UDP_IP, UDP_PORT))
        logging.debug("Addres binded ")


        logging.debug("server start listeing")


        while True:

            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            logging.debug("Recive from {}. Message: {}".format(addr, data))
