from threading import Thread
from time import sleep
from datetime import datetime

def formatted_time():
    return datetime.now().strftime("%a %b %d %Y %H:%M:%S.%f")

def number_power(number, power, task_name):
    sleep_seconds = power
    print(f"Task {task_name} started at: {formatted_time()}")
    print(number ** power)
    sleep(sleep_seconds)
    print(f"Task {task_name} finished at: {formatted_time()}")

def main():
    t1 = Thread(target=number_power, args=(5, 3, 'cube',))
    t2 = Thread(target=number_power, args=(5, 2, 'square',))
    tasks = [t1, t2]

    for task in tasks:
        task.start()

    print("Waiting for thread to finish")
    
    for task in tasks:
        task.join()

    print("Thread finished at: ", formatted_time())

if __name__ == '__main__':
    main()