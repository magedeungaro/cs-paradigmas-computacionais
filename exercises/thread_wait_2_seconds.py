from threading import Thread
from time import sleep
import time

def print_time():
    print(f"Started at: {time.ctime()}")
    sleep(2)
    print(f"Finished at: {time.ctime()}")

def main():
    t1 = Thread(target=print_time)
    t1.start()
    t1.join()

if __name__ == '__main__':
    main()