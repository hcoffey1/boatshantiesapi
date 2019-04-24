#!usr/bin/python3

import time
import multiprocessing import Process
import signal, psutil

def child():
    return

def main():
    with open('time.txt', 'r') as file:
        time = file.readline()
        time = int(time)
        p = process(target = child)
        p.start()
        start_time = time.time()
        # run child process and check every 10 seconds to see if it is time to end the simulation
        while(1):
            time.sleep(10)
            if((time.time() - start_time) / 60 >= time):
                parent = psutil.Process(p.pid)
                children = parent.children(recursive=True)
                for process in children:
                    process.send_signal(signal.SIGTERM)
                break
