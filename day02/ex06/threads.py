import _thread
import time

def runForNMinutes(threadName, minutes):
        time.sleep(60 * minutes)

try:
    _thread.start_new_thread(runForNMinutes, ("Thread-1", 1))
    _thread.start_new_thread(runForNMinutes, ("Thread-2", 2))
    _thread.start_new_thread(runForNMinutes, ("Thread-3", 3))
    _thread.start_new_thread(runForNMinutes, ("Thread-4", 4))
    _thread.start_new_thread(runForNMinutes, ("Thread-5", 5))
except:
    print ("Error")

while 1:
    pass
