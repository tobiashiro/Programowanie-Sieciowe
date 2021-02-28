from server import Server
from client import Client
import threading

serv = Server()
cli = Client()

eventStart = threading.Event()
eventStop = threading.Event()

th1 = threading.Thread(target=serv.run, args=(eventStart, eventStop))
th2 = threading.Thread(target=cli.run, args=(eventStart, eventStop))

th1.start()
th2.start()

th1.join()
th2.join()