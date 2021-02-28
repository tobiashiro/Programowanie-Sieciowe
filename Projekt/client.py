import socket, threading, time, temporenc, easygui, wx, sys
from datetime import datetime


class Client:
    def __init__(self, sock=None):
        self.host = None
        self.port = None
        self.frequency = None
        self.eventStop = None
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def convert_to_iso(self, time_serv):
        return datetime.fromtimestamp(time_serv).isoformat()

    def break_connection(self, event):
        msg = "Do you want to quit?"
        title = "Please Confirm"
        if easygui.ccbox(msg, title):
            event.set()
            self.eventStop.set()
            self.sock.close()
            print("braking connection")
            exit(1)
        else:  # user chose Cancel
            sys.exit(0)

    def get_server_time(self, event):
        while True:
            if event.isSet():
                print("Client close connection. Flag is set")
                exit(1)
                break
            time_1 = time.time_ns() / 1000000
            t_serv = self.sock.recv(1024)
            t_serv = t_serv.decode('utf-8')
            time_2 = time.time_ns() / 1000000
            Tcli = time.time()
            avg_time = (time_2 - time_1)/2
            delta = float(t_serv) + avg_time - time_2
            result_delta = "Delta: {} ms\n".format(round(delta, 3))
            print("Client: " + result_delta)
            print("Server ISOtime: {}".format(self.convert_to_iso(Tcli+delta)))
            time.sleep((int(self.frequency) / 1000))
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, int(self.port)))

    def connect(self):
        try:
            self.sock.connect((self.host, int(self.port)))
            print("Server connected")
            self.run_client_worker()
        except Exception as e:
            print("Connection problem. Error name {}. TRY AGAIN!".format(e))
            self.input_data()

    def run_client_worker(self):
        event = threading.Event()
        th1 = threading.Thread(target=self.get_server_time, args=(event, ))
        th2 = threading.Thread(target=self.break_connection, args=(event,))
        th1.start()
        th2.start()

    def input_data(self):
        while True:
            problems = False
            msg = "Enter client information: "
            title = "Client"
            fieldNames = ["TCP server IP or domain name (default: localhost): ", "Listening port (default - 7): ",
                          "frequency of requests to server between (10 - 1000)"]
            fieldValues = []  # we start with blanks for the values
            fieldValues = easygui.multenterbox(msg, title, fieldNames)
            self.host = fieldValues[0]
            if fieldValues[0] == '':
                self.host = "127.0.0.1"
            else:
                try:
                    socket.inet_aton(self.host)
                except Exception as e:
                    problems = True

            self.port = fieldValues[1]
            if fieldValues[1] == '':
                self.port = 7
            else:
                try:
                    tmp_port = int(fieldValues[0])
                except Exception as e:
                    problems = True

            self.frequency = fieldValues[2]
            try:
                if 10 <= int(self.frequency) <= 1000:
                    self.connect()
                    break
                else:
                    problems = True
            except Exception as e:
                problems = True

            if problems == True:
                errmsg = "You Put iccorrect format. Try again"
                fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
            else:
                break

    def run(self, eventStart, eventStop):
        self.eventStop = eventStop
        eventStart.wait()
        eventStart.clear()
        print("start client")
        self.input_data()
