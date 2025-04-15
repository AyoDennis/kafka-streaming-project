from confluent_kafka import Consumer
import time

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'consumer1',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})
