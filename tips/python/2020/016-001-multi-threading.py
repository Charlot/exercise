import threading
import os
import logging
import time


logging.basicConfig(level=logging.DEBUG,
format='%(filename)s-%(funcName)s-%(lineno)d-%(threadName)s-%(thread)d-%(args)s-%(message)s')
def test_thread_name():
    def fn1(*args):
        logging.debug(args)
        print(f'name: {threading.current_thread().name}--nativeid--{threading.current_thread().native_id}--pid--{os.getpid()}--ident--{threading.current_thread().ident}')
    
    ts = []
    for i in range(0,3):
        # name 是0，默认为 Thread-1
        t = threading.Thread(target=fn1,args=(1,1,3))
        ts.append(t)
        t.start()
    for t in ts:
        t.join()


def test_enumerate():
    def fn():
        print(threading.current_thread().native_id)
    
    ts = []
    for i in range(5):
        time.sleep(1)

        t = threading.Thread(target=fn)
        ts.append(t)
        t.setDaemon(True)
        t.start()

    main_t = threading.current_thread()
    for t in threading.enumerate():
        print(t.is_alive())
        if t is main_t:
            continue
        t.join()


def test_timer():
    class CustomerTimer(threading.Thread):
        def __init__(self, interval, function, args=[], kwargs={}):
            super().__init__()
            self.interval = interval
            self.function  = function
            self.args = args
            self.kwargs = kwargs
            self.finished = threading.Event()
        
        def cancel(self):
            self.finished.set()

        def run(self):
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
            self.finished.set()
            
    ct = CustomerTimer(1, lambda: print(1))
    ct.start()

            
test_timer()