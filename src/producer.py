import threading

def initialize():
    print(f"Thread {threading.get_ident}: initializing producer")

def start_producer():
    x = threading.Thread(target=initialize)
    x.start()
    return x
    