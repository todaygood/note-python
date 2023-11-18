from threading import Thread
from multiprocessing import Pool


def loop():
    while True:
        pass


if __name__ == "__main__":

    for i in range(2):
        t = Thread(target=loop)
        t.start()

    while True:
        pass
