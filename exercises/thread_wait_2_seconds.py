from threading import Thread
from time import sleep
from datetime import datetime

def formatted_time():
    return datetime.now().strftime("%a %b %d %Y %H:%M:%S.%f")

def print_time():
    print(f"Task started at: {formatted_time()}")
    sleep(2)
    print(f"Task Finished at: {formatted_time()}")

def main():
    t1 = Thread(target=print_time)
    t1.start()
    print("Waiting for thread to finish")
    t1.join()
    print("Thread finished at: ", formatted_time())

if __name__ == '__main__':
    main()