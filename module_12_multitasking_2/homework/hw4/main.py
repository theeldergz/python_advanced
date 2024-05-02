import threading, logging, queue, time, requests
from datetime import datetime


logging.basicConfig(level=logging.INFO, filename='test_logs.log', filemode='w+',
                    format='%(threadName)s | %(message)s')
logger = logging.getLogger()
que = queue.Queue()


def create_log():
    global que
    for _ in range(20):
        start_timestamp = datetime.now().timestamp()
        data = requests.get(f'http://127.0.0.1:8080/timestamp/{start_timestamp}')
        message = data.text
        if data.status_code == 200:
            logger.info(f'{start_timestamp} {data.text}')
            que.put(logger.info(f'{start_timestamp} {data.text} in QUEUE'))
        time.sleep(1)


def main():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=create_log)
        threads.append(t)
        t.start()
        time.sleep(1)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
