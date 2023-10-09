import json
from queue import Empty
import threading
import time

TIMEOUT=5

def initialize(queue, name):
    print(f"Thread Consumer {name}: initializing consumer")

    start_time = time.time()

    # If the queue is empty, keep trying until either it has some element to retrieve or after certain timeout
    # If the timeout occurs, it means that no producer is still putting elements in the queue
    while True:
        if time.time()-start_time > TIMEOUT:
            print(f"Thread Consumer {name}: no more items found on the queue after waiting")
            break

        try:
            retrieved_json_serialized_item = queue.get()

            # Let's deserialize this json encoded string to a Python object
            item = json.loads(retrieved_json_serialized_item)
            print(f"Thread Consumer {name}: retrieved item {item}")
        except Empty:
            continue

    print(f"Thread Consumer {name}: finished consuming numbers")

def start_consumer(queue, name):
    x = threading.Thread(target=initialize, args=(queue, name,))
    x.start()
    return x