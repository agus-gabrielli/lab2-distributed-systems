from producer import start_producer
from consumer import start_consumer
from shared_queue import SharedQueue

def main():
    # Creating shared queue
    queue = SharedQueue()

    print("Thread Main: creating producers and consumers")

    # Initialize producers 1 and 2
    prod1 = start_producer(queue, "prod1")
    prod2 = start_producer(queue, "prod2")

    # Initialize consumer
    cons1 = start_consumer(queue, "cons1")

    prod1.join()
    prod2.join()
    cons1.join()
    print("Thread Main: finished producer 1")
    print("Thread Main: finished producer 2")
    print("Thread Main: finished consumer 1")
    

if __name__ == "__main__":
    main()