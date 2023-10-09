from producer import start_producer
from consumer import start_consumer

def main():
    # Initialize producers 1 and 2
    prod1 = start_producer()
    prod2 = start_producer()

    # Initialize consumer
    cons = start_consumer()

    prod1.join()
    prod2.join()
    cons.join()
    print("Finished producer 1")
    print("Finished producer 2")
    print("Finished consumer")
    

if __name__ == "__main__":
    main()