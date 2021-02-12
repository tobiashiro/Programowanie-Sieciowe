import threading, logging, sys
import time
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


def program_2():
    global list_of_threads, stop_events
    try:
        lock = threading.Lock()
        for j in range(10):
            th = threading.Thread(target=progr_2_prints, args=(j, lock))
            list_of_threads.append(th)
            th.start()
    except:
        print("crating threads failed")


def progr_2_prints(thread_number, lock):
    try:
        for k in alphabet:
            lock.acquire()
            if thread_number + 1 == 10:
                logging.debug("{}".format(k))

            else:
                logging.debug("{}".format(k))
            time.sleep(1)
            lock.release()
    except:
        print("Looping failed")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
list_of_threads = []
try:
    prog_2 = threading.Thread(target=program_2)
    prog_2.start()
except:
    print("creating thread failed")
    sys.exit(1)
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()