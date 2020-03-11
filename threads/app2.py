import threading
import time
import logging as log


def task(name):
    log.info("Thread %s starting", name)
    time.sleep(2)
    log.info("Thread %s finishing", name)


if __name__ == "__main__":
    log.basicConfig(format="%(asctime)s: %(message)s", level=log.INFO, datefmt="%H:%M:%S")
    log.info("Main : starting")
    start = time.time()

    threads = list()
    for i in range(3):
        log.info("Main    : create and start thread %d", i)
        x = threading.Thread(target=task, args=(i,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        log.info("Main    : before joining thread %d", index)
        thread.join()  # wait for the thread to finish
        log.info("Main    : thread %d done", index)

    duration = time.time() - start
    log.info("duration %d", duration)
