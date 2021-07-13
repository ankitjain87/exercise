import random
import threading
import time


class Broker:
    def __init__(self):
        self.queue = []

    def add_message(self, msg):
        self.queue.append(msg)

    def get_message(self):
        print("Queue size", id(self), len(self.queue))
        return self.queue.pop(0) if len(self.queue) > 0 else None

    def is_there_a_new_message(self):
        return True if len(self.queue) > 0 else False
        

class Producer(threading.Thread):
    def __init__(self, name, broker):
        super(Producer, self).__init__()
        self.name = name
        self.broker = broker

    def push_message(self, msg):
        self.broker.add_message(msg)

    def run(self):
        while True:
            r = random.random()
            self.push_message(r)
            time.sleep(random.randint(1,5))



class Consumer(threading.Thread):
    def __init__(self, name, broker):
        super(Consumer, self).__init__()
        self.name = name
        self.broker = broker

    def get_message(self):
        return self.broker.get_message()
    

    # def notify(self):
    #     print("New Message Received")

    def run(self):
        while True:
            if self.broker.is_there_a_new_message():
                msg = self.get_message()
                print(self.name, msg)
                # time.sleep(random.randint(1,5))



class Consumer2(threading.Thread):
    def __init__(self, name, broker):
        super(Consumer2, self).__init__()
        self.name = name
        self.broker = broker

    def get_message(self):
        return self.broker.get_message()
    

    # def notify(self):
    #     print("New Message Received")

    def run(self):
        while True:
            if self.broker.is_there_a_new_message():
                msg = self.get_message()
                print(self.name, round(msg*10, 2))
                # time.sleep(1)



b1 = Broker()
print("Broker1 ID", id(b1))
p1 = Producer("P1", b1)


b2 = Broker()
print("Broker2 ID", id(b2))
p2 = Producer("P2", b2)

c1 = Consumer("C1", b1)
c2 = Consumer2("C2", b2)


p1.start()
c1.start()

p2.start()
c2.start()