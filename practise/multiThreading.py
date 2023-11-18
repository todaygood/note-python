from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print("开始下载{}".format(filename))
    time_to_download = randint(5, 10)
    sleep(time_to_download)

    print("下载{} 耗费了{}".format(filename, time_to_download))


def main():
    start = time()

    t1 = Thread(target=download, args=('Python1',))
    t1.start()

    t2 = Thread(target=download, args=('Python2',))
    t2.start()

    t1.join()
    t2.join()

    end = time()

    print('总共耗费了%.3f秒' % (end - start))


if __name__ == "__main__":
    main()
