import threading

def initialize():
    print(f"Thread {threading.get_ident}: initializing consumer")

def start_consumer():
    x = threading.Thread(target=initialize)
    x.start()
    return x