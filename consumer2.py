from confluent_kafka import Consumer
import time

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'consumer2',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['my_topic'])

while True:
    msg = c.poll(1.0)
    time.sleep(2)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    message = msg.value().decode('utf-8')
    print(f'Received message from topic => {msg.topic()}, partition => {msg.partition()}')
    c.close()
