import logging
import time

from confluent_kafka import Consumer

logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(20)

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'consumer2',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

logging.info(f"Starting consumer with {conf}")

consumer.subscribe(['my_topic'])

logging.info("Subscribed to my_topic")

while True:
    msg = consumer.poll(1.0)
    time.sleep(2)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    message = msg.value().decode('utf-8')
    logging.info("decoded event")
    logging.info(f"Received message from topic => {msg.topic()}, \
          partition => {msg.partition()}")
consumer.close()
