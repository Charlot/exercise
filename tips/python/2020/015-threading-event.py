import threading
import time
from queue import Queue

class Pub:
    def __init__(self):
        self.pub_event = threading.Event()
        self.q = Queue()
    
    def send(self, msg):
        self.q.put(msg)
        self.pub_event.set()
    
    def pub(self):
        while True:
            self.pub_event.wait()
            msg = self.q.get()
            print(msg)
            if msg==3:
                break
            



pub = Pub()
t = threading.Thread(target=pub.pub)
t.start()
t.isDaemon=True

for i in range(5):
    pub.send(i)
    time.sleep(1)

t.join()