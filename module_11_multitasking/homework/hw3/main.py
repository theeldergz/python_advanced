import logging
import random
import threading
import time
from typing import List

TOTAL_TICKETS: int = 10

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        self.tickets_sold: int = 0
        logger.info('Seller started work')

    def run(self) -> None:
        global TOTAL_TICKETS
        is_running: bool = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.name} sold one;  {TOTAL_TICKETS} left')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self) -> None:
        time.sleep(random.random())


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        self.available_seats: int = 200
        logger.info('Director started work')

    def run(self) -> None:
        global TOTAL_TICKETS
        logger.info(TOTAL_TICKETS)
        is_running: bool = True
        while is_running:
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                if TOTAL_TICKETS <= 4:
                    TOTAL_TICKETS += 4
                    self.available_seats -= 4
                    logger.info(f'{self.name} Director print {4} tickets')
                    logger.info(f'Available seats: {self.available_seats}')
                if self.available_seats <= 0:
                    is_running: bool = False
                    logger.info('All seats occupied')




def main() -> None:
    semaphore: threading.Semaphore = threading.Semaphore()
    sellers: List[Seller] = []

    director = Director(semaphore)
    director.start()

    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()




if __name__ == '__main__':
    main()
