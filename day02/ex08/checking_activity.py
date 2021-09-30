import psutil

def main():
    for proc in psutil.process_iter():
        try:
        # Get process name & pid from process object.
            processID = proc.pid
            processStatus = proc.status()
            #processPriority = proc.priority
            ##processCpu = proc

            print(str(processID) + " | " + processStatus)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    main()
