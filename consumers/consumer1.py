import logging
import time

from confluent_kafka import Consumer

logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(20)

consumer_configuration = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'consumer1',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_configuration)

logging.info(f"Starting consumer with {consumer_configuration}")

consumer.subscribe(['demo_topic'])

logging.info("Subscribed to demo_topic")

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
logging.info("Connection closed unexpectedly")
