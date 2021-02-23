import sys, logging,  struct, socket, time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s, ) %(message)s',)


class MulticastServer:

    def __init__(self):
        self.multicast_group = ""
        self.server_address = ('', 7)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def create_socket(self, event):
        logging.debug("Multicast Server start")
        time.sleep(0.5)
        try:
            self.multicast_group = str(input("UDP SERVER IP or domain name (default: 224.3.29.71): "))
            if len(self.multicast_group) == 0:
                self.multicast_group = "224.3.29.71"
            self.server_address = input("Listening port (default - 7): ")
            if len(self.server_address) == 0:
                self.server_address = ('', 7)
            else:
                raise Exception("You put incorrect format")
            self.sock.bind(self.server_address)
        except Exception as e:
            logging.debug("Error during input data. Error name {}".format(e))

        group = socket.inet_aton(self.multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        event.set()

        while True:
            logging.debug('Server waiting to receive message')
            data, address = self.sock.recvfrom(1024)

            logging.debug("received {} bytes from: {}".format(data, address))

            logging.debug("sending acknowledgement to: {}".format(address))
            self.sock.sendto(bytes('ack'.encode()), address)

    def run(self, event):
        self.create_socket(event)
