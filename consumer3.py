from confluent_kafka import Consumer
import time

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'consumer3',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})
