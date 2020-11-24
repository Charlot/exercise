import threading
import os
import logging
import time
import collections

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


def test_customer_queue():
    class CustomerQueue():
        def __init__(self, maxsize=0):
            self.maxsize = maxsize
            self.mutex = threading.Lock()
            self.not_empty = threading.Condition(self.mutex)
            self.not_full = threading.Condition(self.mutex)
            self._queue = collections.deque()
            self.maxsize = maxsize

        def size(self):
            with self.mutex:
                return len(self._queue)

        def empty(self):
            with self.mutex:
                return self._size()==0
        
        def full(self):
            with self.mutex:
                return 0<self.maxsize<=self._size()


        def get(self, block=True, timeout=None):
            self.not_empty.acquire()
            try:
                if not block:
                    if self.size()==0:
                        raise Exception('empty')
                if timeout is None:
                    while not self._size():
                        self.not_empty.wait()

                elif timeout<0:
                    raise Exception('timeout cannot <0')
                else:
                    endtime = time.time()+timeout
                    while not self._size():
                        remaining = endtime - time.time()
                        if remaining<=0:
                            raise Exception('timeout')
                        self.not_empty.wait(remaining)

                item = self._get()
                self.not_full.notify()
                return item
            finally:
                self.not_empty.release()

        def put(self, item, block=True, timeout=None):
            self.not_full.acquire()
            try:
                if self.maxsize>0:
                    if not block:
                        if self._size()>=self.maxsize:
                            raise Exception('full')
                    elif timeout is None:
                        while self._size()>=self.maxsize:
                            self.not_full.wait()
                    else:
                        endtime = time.time()+timeout
                        while self._size()>=self.maxsize:
                            remaining = endtime - time.time()
                            if remaining<=0:
                                raise Exception('full timeout')
                            self.not_full.wait(remaining)
                self._put(item)
                self.not_empty.notify()
            finally:
                self.not_full.release()


        
        def _size(self):
            return len(self._queue)

        def _get(self):
            return self._queue.pop()

        def _put(self, item):
            self._queue.append(item)


test_timer()