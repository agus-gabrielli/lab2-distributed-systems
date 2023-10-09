# lab2-distributed-systems

## Exercise Producer-Consumer System with JSON Serialization/Deserialization 

### Scenario
Create a producer-consumer system in Python with two producers and one consumer. The producers will generate data, serialize it to JSON, and place it in a shared queue. The consumer will retrieve items from the queue, deserialize them from JSON, and process them. 

### Requirements

1. Create a shared queue (e.g., using Python's queue.Queue module) that can hold a limited number of JSON-serialized items (e.g., dictionaries or objects). 

2. Implement two producer functions, producer1 and producer2, which generate random data, serialize it to JSON, and place it in the shared queue. Each producer should run in its own thread. 

3. Implement a consumer function which retrieves items from the shared queue, deserializes from JSON, and processes them. The consumer should run in its own thread as well. 

4. Ensure proper synchronization between producers and the consumer using Python's threading mechanisms (e.g., threading.Lock). 

5. Utilize a JSON library in Python (e.g., the json module) for serialization and deserialization. 

6. Start both producer threads and the consumer thread, and demonstrate the concurrent behavior of the system.

## Execution

To execute the program, run

 ``` python3 main.py ```

 ## Output example
```
Thread Main: creating producers and consumers
Thread Producer prod1: initializing producer
Thread Producer prod2: initializing producer
Thread Producer prod2: just put {'item': 26453}
Thread Producer prod2: just put {'item': 52930}
Thread Producer prod2: just put {'item': 69553}
Thread Producer prod1: just put {'item': 26364}
Thread Consumer cons1: initializing consumer
Thread Producer prod1: just put {'item': 14842}
Thread Consumer cons1: retrieved item {'item': 26364}
Thread Producer prod1: just put {'item': 63933}
Thread Consumer cons1: retrieved item {'item': 26453}
Thread Producer prod1: just put {'item': 51615}
Thread Consumer cons1: retrieved item {'item': 52930}
Thread Producer prod1: just put {'item': 76516}
Thread Consumer cons1: retrieved item {'item': 69553}
Thread Producer prod1: just put {'item': 43345}
Thread Producer prod2: just put {'item': 39177}
Thread Producer prod1: just put {'item': 61394}
Thread Producer prod2: just put {'item': 87297}
Thread Producer prod1: just put {'item': 1627}
Thread Producer prod2: just put {'item': 16427}
Thread Producer prod1: just put {'item': 39760}
Thread Consumer cons1: retrieved item {'item': 39177}
Thread Consumer cons1: retrieved item {'item': 14842}
Thread Consumer cons1: retrieved item {'item': 63933}
Thread Producer prod1: just put {'item': 58791}
Thread Producer prod1: just put {'item': 96292}
Thread Producer prod2: just put {'item': 26951}
Thread Consumer cons1: retrieved item {'item': 51615}
Thread Consumer cons1: retrieved item {'item': 76516}
Thread Consumer cons1: retrieved item {'item': 43345}
Thread Producer prod1: just put {'item': 8444}
Thread Producer prod1: just put {'item': 40829}
Thread Producer prod2: just put {'item': 59551}
Thread Consumer cons1: retrieved item {'item': 61394}
Thread Consumer cons1: retrieved item {'item': 87297}
Thread Producer prod2: just put {'item': 27359}
Thread Consumer cons1: retrieved item {'item': 1627}
Thread Consumer cons1: retrieved item {'item': 16427}
Thread Consumer cons1: retrieved item {'item': 39760}
Thread Consumer cons1: retrieved item {'item': 58791}
Thread Consumer cons1: retrieved item {'item': 26951}
Thread Consumer cons1: retrieved item {'item': 96292}
Thread Consumer cons1: retrieved item {'item': 8444}
Thread Consumer cons1: retrieved item {'item': 59551}
Thread Consumer cons1: retrieved item {'item': 40829}
Thread Producer prod1: just put {'item': 28347}
Thread Consumer cons1: retrieved item {'item': 27359}
Thread Producer prod2: just put {'item': 5079}
Thread Producer prod2: just put {'item': 94111}
Thread Producer prod2: just put {'item': 54507}
Thread Producer prod2: just put {'item': 4055}
Thread Producer prod2: just put {'item': 45305}
Thread Producer prod1: just put {'item': 26399}
Thread Producer prod2: just put {'item': 39751}
Thread Producer prod1: just put {'item': 68038}
Thread Consumer cons1: retrieved item {'item': 28347}
Thread Consumer cons1: retrieved item {'item': 5079}
Thread Consumer cons1: retrieved item {'item': 94111}
Thread Consumer cons1: retrieved item {'item': 54507}
Thread Consumer cons1: retrieved item {'item': 4055}
Thread Producer prod2: just put {'item': 84869}
Thread Consumer cons1: retrieved item {'item': 45305}
Thread Consumer cons1: retrieved item {'item': 26399}
Thread Producer prod2: just put {'item': 46546}
Thread Producer prod1: just put {'item': 41173}
Thread Producer prod1: just put {'item': 13018}
Thread Producer prod1: just put {'item': 87022}
Thread Producer prod1: just put {'item': 94053}
Thread Producer prod1: finished producing numbers
Thread Consumer cons1: retrieved item {'item': 39751}
Thread Producer prod2: just put {'item': 49358}
Thread Producer prod2: just put {'item': 7821}
Thread Producer prod2: just put {'item': 67634}
Thread Producer prod2: finished producing numbers
Thread Consumer cons1: retrieved item {'item': 68038}
Thread Consumer cons1: retrieved item {'item': 84869}
Thread Consumer cons1: retrieved item {'item': 41173}
Thread Consumer cons1: retrieved item {'item': 46546}
Thread Consumer cons1: retrieved item {'item': 49358}
Thread Consumer cons1: retrieved item {'item': 13018}
Thread Consumer cons1: retrieved item {'item': 87022}
Thread Consumer cons1: retrieved item {'item': 94053}
Thread Consumer cons1: retrieved item {'item': 7821}
Thread Consumer cons1: retrieved item {'item': 67634}
Thread Consumer cons1: no more items found on the queue after waiting
Thread Consumer cons1: finished consuming numbers
Thread Main: finished producer 1
Thread Main: finished producer 2
Thread Main: finished consumer 1
```