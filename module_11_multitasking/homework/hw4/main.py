import queue
import random
from queue import PriorityQueue
import threading
import time


class Producer(threading.Thread):
    def __init__(self, queue, task, task_count=10):
        super().__init__()
        self.queue = queue
        self.task_count = task_count
        self.task = task
        self.running = True

    def run(self):
        while self.running:
            print('Producer: Running')
            for i in range(self.task_count):
                priority = random.randint(0, 10)
                self.queue.put((priority, task))
            self.running = False
            print('Producer: Done')



class Consumer(threading.Thread):
    def __init__(self, queue: PriorityQueue):
        super().__init__()
        self.queue = queue
        self.running = True

    def run(self):
        while self.running:
            print('Consumer: Running')
            for i in range(self.queue.qsize()):
                new_task = self.queue.get()
                new_task[1].run(priority=new_task[0])
                self.queue.task_done()
            print('Consumer: Done')
            self.running = False


class Task:
    def run(self, priority):
        runtime = random.random()
        time.sleep(runtime)
        print(f'>running Task(priority={priority}),   sleep({runtime})')


if __name__ == '__main__':
    task_count = 10
    priority_queue = PriorityQueue()
    task = Task()
    p = Producer(queue=priority_queue, task=task)
    p.start()
    cons = Consumer(queue=priority_queue)
    cons.start()

    priority_queue.join()