import socket, logging, threading, sys

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class Client:

    def __init__(self):
        self.host: str
        self.port: int
        self.host = ""
        self.port = 0

    def start_client(self, event):
        try:
            logging.debug("Client start")
            self.host = str(input("UDP server IP or domain name (default: localhost): "))
            if len(self.host) == 0:
                self.host = "127.0.0.1"
            self.port = input("Listening port (default - 7): ")
            if len(self.port) == 0:
                self.port = 7
            elif self.port.isnumeric():
                port = int(self.port)
            else:
                raise Exception("You put incorrect format")
        except Exception as e:
            logging.warning("You put incorrect input data. Exepction message: ".format(e))
            sys.exit(1)

        logging.debug("If you want to finish - type 'quit' ")
        event.set()

        thread_list = []

        while True:
            try:
                msg = str(input("Type your message: "))
                if msg == 'quit':
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.close()
                    break
                MESSAGE = str.encode(msg)

                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                th = threading.Thread(target=sock.sendto(MESSAGE, (self.host, self.port)))
                thread_list.append(th)
                logging.debug("Mesage has sent")
            except Exception as e:
                logging.warning("Error during sending message. Error message: ".format(e))
                sys.exit(1)





