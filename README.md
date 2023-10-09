# lab2-distributed-systems

## Exercise Producer-Consumer System with JSON Serialization/Deserialization 

### Scenario
Create a producer-consumer system in Python with two producers and one consumer. The producers will generate data, serialize it to JSON, and place it in a shared queue. The consumer will retrieve items from the queue, deserialize them from JSON, and process them. 

### Requirements

1. Create a shared queue(e.g., usingPython'squeue.Queuemodule) thatcan holda limited numberof JSON-serializeditems (e.g., dictionariesor objects). 

2. Implement two producer functions, producer1 and producer2, whichgenerate random data, serializeitto JSON, and place itin the sharedqueue. Eachproducer shouldrunin itsownthread. 

3. Implementa consumer functionwhichretrievesitems from the sharedqueue, deserializes from JSON, and processesthem. The consumer shouldrunin itsownthreadaswell. 

4. Ensurepropersynchronizationbetweenproducers and the consumer usingPython's threading mechanisms(e.g., threading.Lock). 

5. Utilizea JSON library in Python (e.g., the jsonmodule) for serializationand deserialization. 

6. Start bothproducer threadsand the consumer thread, and demonstratethe concurrent behaviorof the system.

## Execution

To execute the program, run

 ``` python3 main.py ```