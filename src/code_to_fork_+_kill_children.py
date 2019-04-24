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
        while(1):
            sleep(10)
            if(time.time() - start_time >= time):
                parent = psutil.Process(p.pid)
                children = parent.children(recursive=True)
                for process in children:
                    process.send_signal(signal.SIGTERM)
