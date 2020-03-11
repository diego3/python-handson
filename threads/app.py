import threading
import time
import logging as log


def task(n):
    log.info("Thread %s starting", n)
    time.sleep(2)
    log.info("Thread %s finishing", n)


if __name__ == "__main__":
    log.basicConfig(format="%(asctime)s: %(message)s", level=log.INFO, datefmt="%H:%M:%S")
    log.info("Main : starting")
    start = time.time()

    log.info("Main    : before creating thread")
    x = threading.Thread(target=task, args=(1,), daemon=True)
    log.info("Main    : before running thread")
    x.start()
    log.info("Main    : wait for the thread to finish")
    x.join()  # wait for the thread to finish
    log.info("Main    : all done")

    duration = time.time() - start
    log.info("duration %d", duration)
