from multicastClient import MulticastClient
from multicastServer import MulticastServer
from broadcastClient import BroadcastClient
from broadcastServer import BroadcastServer



import threading, time, logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s, MAIN THREAD) %(message)s',)

# event that informs that the server has binded address. Client can start
event = threading.Event()

sending_method = str(input("Choose your techniqe: 'm' for multicast or 'b' for broadcast: "))

if sending_method == "m":
    mc = MulticastClient()
    ms = MulticastServer()
    th1 = threading.Thread(target=mc.run, args=(event,))
    th2 = threading.Thread(target=ms.run, args=(event,))
    th2.start()
    th1.start()
    th1.join()
    th2.join()

elif sending_method == "b":
    bc = BroadcastClient()
    bs = BroadcastServer()
    th1 = threading.Thread(target=bc.run, args=(event,))
    th2 = threading.Thread(target=bs.run, args=(event,))
    th2.start()
    th1.start()
    th1.join()
    th2.join()

else:
    logging.debug("You put incorrect symbol")


