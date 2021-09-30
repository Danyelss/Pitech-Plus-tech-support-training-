import _thread
import time
import sys
import os
from subprocess import Popen, PIPE
import subprocess



def second_thread_function(threadName, minutes):
    time.sleep(120)

def first_thread_function(threadName, minutes):
    #process = Popen(['python3', 'process.py', '1', '1', '1', '1'])
    subprocess.run(["python3", "process.py", '1', '1', '1', '1']) 
    time.sleep(60 * minutes)


def main():
    if len(sys.argv) == 1 :
        try:
            _thread.start_new_thread(first_thread_function, ("Thread-1", 2))
            _thread.start_new_thread(first_thread_function, ("Thread-1", 2))
            _thread.start_new_thread(first_thread_function, ("Thread-1", 2))
            _thread.start_new_thread(first_thread_function, ("Thread-1", 2))
            _thread.start_new_thread(first_thread_function, ("Thread-1", 2))
        except:
            print ("Error 1")
    elif len(sys.argv) == 5 :
        try:
            _thread.start_new_thread(second_thread_function, ("Thread-1", 2))
            _thread.start_new_thread(second_thread_function, ("Thread-1", 2))
            _thread.start_new_thread(second_thread_function, ("Thread-1", 2))
        except:
            print ("Error 2")

    time.sleep(60 * 2)

if __name__ == "__main__":
    main()