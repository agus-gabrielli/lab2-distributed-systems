from queue import Queue
from threading import Lock

MAX_ITEMS=10


class SharedQueue:
    def __init__(self):
        self._lock = Lock()
        self._queue = Queue(maxsize=MAX_ITEMS)

    # Non blocking. Raises Empty exception if queue is empty
    def get(self):
        with self._lock:
            return self._queue.get_nowait()
    
    # Non blocking. Raises Full exception if queue is full
    def put(self, item):
        with self._lock:
            self._queue.put_nowait(item)