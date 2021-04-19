from kafka import KafkaProducer
import random
import time


class MyProducer(object):
    def __init__(self, intervals):
        self.intervals = intervals

    def start_produce(self):
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        while 1:
            value = random.randint(0, 1000)
            timestamp = time.time()
            timestamp = bytes(str(timestamp), encoding='UTF-8')
            value = bytes(str(value), encoding='UTF-8')
            future = producer.send('my_topic', key=timestamp, value=value, partition=0)
            result = future.get(timeout=10)
            print(result)
            time.sleep(self.intervals)


if __name__ == "__main__":
    res = MyProducer(intervals=1)
    res.start_produce()
