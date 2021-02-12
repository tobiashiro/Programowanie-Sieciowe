import threading
import time, sys
import easygui


def program_1():
    print("Hello world")


def program_2():
    global list_of_threads
    try:
        for i in range(10):
            lock = threading.Event()
            th = threading.Thread(target=progr_2_prints, args=(i, lock, ))
            list_of_threads.append(th)
            lock_list.append(lock)
    except:
        print("Error during looping")
        sys.exit(1)


def progr_2_prints(thread_number, lock):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    global stop_th, value_command
    try:
        for i in alphabet:
            if stop_th-1 == thread_number and value_command == "STOP":
                print("Thread {} has stopped".format(thread_number+1))
                lock.wait()
            if thread_number+1 == 10:
                print("{}{}".format(i, 0))
            else:
                print("{}{}".format(i, thread_number+1))
            time.sleep(1)
    except:
        print("Error during looping")
        sys.exit(1)


def stop_thread():
    try:
        global stop_th, value_command, list_of_started_threads
        while True:
            msg = "Manage threads"
            title = "What do you want to do?"
            fieldNames = ["Command", "Number of thread"]
            fieldValues = easygui.multenterbox(msg, title, fieldNames)
            if fieldValues is None:
                sys.exit(0)
            # make sure that none of the fields were left blank
            while 1:
                errmsg = ""
                for i, name in enumerate(fieldNames):
                    if fieldValues[i].strip() == "":
                        errmsg += "{} is a required field.\n\n".format(name)
                tmp_val = fieldValues[0]
                if tmp_val.upper() != "START" and tmp_val.upper() != "STOP":
                    errmsg += "Please use 'START' or 'STOP'"
                try:
                    if not isinstance(int(fieldValues[1]), int):
                        errmsg += "Please use integers to start threads"
                except:
                    errmsg += "Please use integers to start threads"
                try:
                    if int(fieldValues[1]) > 10:
                        errmsg += "Number of threads is 10. Please choose smaller digit"
                except:
                    "Please use integers to start threads"
                if errmsg == "":
                    break  # no problems found
                fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
                if fieldValues is None:
                    break

            value_command = fieldValues[0].upper()
            stop_th = int(fieldValues[1])
            if value_command == "START":
                if stop_th-1 not in list_of_started_threads:
                    list_of_threads[stop_th-1].start()
                    list_of_started_threads.append(stop_th-1)
                elif stop_th-1 in list_of_started_threads:
                    print("release {}".format(stop_th))
                    tmp_lock = lock_list[stop_th-1]
                    tmp_lock.set()
    except:
        print("Error during getting data")
        sys.exit(1)


list_of_started_threads = []
lock_list = []
list_of_threads = []
stop_th = int()
value_command = None
try:
    prog_1 = threading.Thread(target=program_1)
    prog_1.start()
    prog_1.join()
    prog_2 = threading.Thread(target=program_2)
    prog_2.start()
    prog_3 = threading.Thread(target=stop_thread)
    prog_3.start()
except:
    print("creating threads failed")
    sys.exit(1)
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()


