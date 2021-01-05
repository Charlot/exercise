# https://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p10_defining_an_actor_task.html

from queue import Queue
import threading
from threading import Event

class CloseException(Exception):
    pass

class Actor:
    
    def __init__(self):
        self.queue = Queue()
    
    def receive(self):
        msg = self.queue.get()
        if msg is CloseException:
            raise CloseException()
        return msg
                

    def send(self,msg):
        self.queue.put(msg)


    def start(self):
        self._close_event = Event()
        t = threading.Thread(target=self._bootstrap)

        t.isDaemon=True   
        t.start()

    def join(self):
        self._close_event.wait()

    def _bootstrap(self):
        try:
            self.run()
        except CloseException as ex:
            print(f'close...{ex}')
        finally:
            self._close_event.set()

        
    def close(self):
        self.send(CloseException)

    def run(self):
        while True:
            self.receive()

class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.receive()
            print(f'received msg: {msg}')
            
a = PrintActor()
a.start()
# a.send(1)
# a.send(3)
# a.close()
# a.join()
# print(111)
input1  = input('请输入:')
while input1:
    if input1=='q':
        a.close()
        a.join()
        break
    a.send(input1)
    input1 = input('请输入:')

print('closed.....')