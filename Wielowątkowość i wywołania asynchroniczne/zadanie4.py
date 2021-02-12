import threading, asyncio
import time, sys
import easygui


def program_2():
    global list_of_threads
    for i in range(10):
        try:
            lock = threading.Event()
            th = threading.Thread(target=progr_2_prints, args=(i, lock, ))
            list_of_threads.append(th)
            lock_list.append(lock)
            th.start()
        except:
            print("Error during creating threads")
            sys.exit(1)


def loop_inside_thread(alphabet, thread_number, lock):
    global stop_th
    try:
        for i in alphabet:
            if stop_th-1 == thread_number:
                print("Thread {} has stopped".format(thread_number+1))
                lock.wait()
            if thread_number+1 == 10:
                print("{}{}".format(i, 0))
            else:
                print("{}{}".format(i, thread_number+1))
            time.sleep(1)
    except:
        print("error during looping in thread number: {}".format(thread_number))
        sys.exit(1)


def progr_2_prints(thread_number, lock):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    global stop_th, value_command
    try:
        asyncio.create_task(loop_inside_thread(alphabet, thread_number, lock))
    except:
        print("Fished job")
        sys.exit(1

                 )
def stop_thread():
    global stop_th, value_command, list_of_started_threads
    try:
        while True:
            msg = "Select thread"
            title = "Which thread do you want to stop?"
            fieldNames = ["Number of thread"]
            fieldValues = easygui.multenterbox(msg, title, fieldNames)
            if fieldValues is None:
                sys.exit(0)
            # make sure that none of the fields were left blank
            while 1:
                errmsg = ""
                for i, name in enumerate(fieldNames):
                    if fieldValues[i].strip() == "":
                        errmsg += "{} is a required field.\n\n".format(name)
                try:
                    if not isinstance(int(fieldValues[0]), int):
                        errmsg += "Please use integers to start threads"
                except:
                    errmsg += "Please use integers to start threads"
                try:
                    if int(fieldValues[0]) > 10:
                        errmsg += "Number of threads is 10. Please choose smaller digit"
                except:
                    "Please use integers to start threads"
                if errmsg == "":
                    break  # no problems found
                fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
                if fieldValues is None:
                    break

            stop_th = int(fieldValues[0])
    except:
        print("Error while getting commands")
        sys.exit(1)


def main():
    try:
        prog_2 = threading.Thread(target=program_2)
        prog_2.start()
    except:
        print("errror during creating threads")
        sys.exit(1)


list_of_started_threads = []
lock_list = []
list_of_threads = []
stop_th = int()
value_command = None
main()
prog_3 = threading.Thread(target=stop_thread)
prog_3.start()
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()


