import socket, logging
import struct
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class MulticastClient:

    def __init__(self):
        self.message: str
        self.host: str
        self.port: int
        self.host = ""
        self.port = 0
        self.multicast_group = (self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start_client(self, event):
        try:
            logging.debug("Multicast Client start")
            self.message = bytes(input("Type your Multi-message: "))
            self.host = str(input("UDP server IP or domain name (default: 224.3.29.71): "))
            if len(self.host) == 0:
                self.host = "224.3.29.71"
            self.port = input("Listening port (default - 7): ")
            if len(self.port) == 0:
                self.port = 7
            elif self.port.isnumeric():
                self.port = int(self.port)
            else:
                raise Exception("You put incorrect format")

            self.multicast_group = ('{}'.format(self.host), self.port)
        except Exception as e:
            logging.warning("You put incorrect input data. Exepction message: {}".format(e))
            sys.exit(1)

        logging.debug("If you want to finish - type 'quit' ")

    def create_datagram_socket(self):
        # Set a timeout so the socket does not block indefinitely when trying
        # to receive data.
        self.sock.settimeout(0.2)
        ttl = struct.pack('b', 1)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    def send_message(self):
        try:
            # Send data to the multicast group
            logging.debug("Sending message to multicast: {}".format(self.message))
            self.sock.sendto(self.message, self.multicast_group)
            # Look for responses from all recipients
            while True:
                logging.debug("waiting to recive")
                try:
                    data, server = self.sock.recvfrom(16)
                except self.socket.timeout:
                    logging.debug('timed out, no more responses')
                    break
                else:
                    logging.debug("received {} from {}".format(data, server))

        finally:
            logging.debug("closing socket")
            self.sock.close()

