import time
import threading
import multiprocessing

def delayForThreads(minutes):
    time.sleep( 60 * minutes )

def first_thread_function(numberOfThreads):
    threads = []
    for i in range(numberOfThreads):
        thread = threading.Thread(target=delayForThreads, args=(1,))
        threads.append(thread)
        threads[i].start()

    for i in range(numberOfThreads):
        threads[i].join()

def main():
    processes = []
    for i in range(5):
        proces = multiprocessing.Process(target=first_thread_function, args=(3,))
        processes.append(proces)
        processes[i].start()

    for i in range(5):
        processes[i].join()

if __name__ == "__main__":
    main()