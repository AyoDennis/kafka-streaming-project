from confluent_kafka import Consumer
import time

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'consumer3',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['my_topic', 'my_topic2'])

while True:
    msg = c.poll(1.0)
    time.sleep(2)
