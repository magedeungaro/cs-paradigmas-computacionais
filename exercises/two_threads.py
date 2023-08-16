from threading import Thread
from time import sleep
from datetime import datetime

def formatted_time():
    return datetime.now().strftime("%a %b %d %Y %H:%M:%S.%f")

def print_time(sleep_seconds, task_name):
    print(f"Task {task_name} started at: {formatted_time()}")
    sleep(sleep_seconds)
    print(f"Task {task_name} finished at: {formatted_time()}")

def main():
    tasks = [Thread(target=print_time, args=(3, 'one',)), Thread(target=print_time, args=(2, 'two',))]

    for task in tasks:
        task.start()

    print("Waiting for threads to finish")

    for task in tasks:
        task.join()

    print("Threads finished at: ", formatted_time())

if __name__ == '__main__':
    main()