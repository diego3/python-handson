import concurrent.futures
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(task, range(3))

    duration = time.time() - start
    log.info("duration %d", duration)
