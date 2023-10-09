import json
from queue import Full
import random
import threading

NUMBER_OF_ITEMS_TO_INSERT=20
MAX_INT_RAND_NUMBER=100000

def initialize(queue, name):
    print(f"Thread Producer {name}: initializing producer")

    # Insert NUMBER_OF_ITEMS_TO_INSERT dictionaries with random numbers in the queue
    for _ in range(NUMBER_OF_ITEMS_TO_INSERT):
        random_number = random.randint(0,MAX_INT_RAND_NUMBER)
        item = {"item": random_number}

        # Let's serialize the Python dictionary to a json string
        json_serialized_item = json.dumps(item)

        # If the queue is full, try until it frees some space
        while True:
            try:
                queue.put(json_serialized_item)
                print(f"Thread Producer {name}: just put {item}")
                break
            except Full:
                continue

    print(f"Thread Producer {name}: finished producing numbers")

def start_producer(queue, name):
    x = threading.Thread(target=initialize, args=(queue, name,))
    x.start()
    return x
    