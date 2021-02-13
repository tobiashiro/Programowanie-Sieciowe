from client import Client
from server import Server
import threading, sys, time, logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

cl = Client()
sv = Server()

event = threading.Event()

th2 = threading.Thread(target=sv.start_server)
th2.start()
time.sleep(1)

list_of_threads = []

try:
    number_of_clients = int(input("Type numer of clients: "))
except Exception as e:
    print("You put incorrect format. ")
    sys.exit(1)

for client in range(number_of_clients):
    event.clear()
    th = threading.Thread(target=cl.start_client(event))
    event.wait()
    list_of_threads.append(th)
    logging.debug("Thread number {} finished work".format(client+1))

















