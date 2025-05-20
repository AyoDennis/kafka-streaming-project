from dotenv import load_dotenv

load_dotenv()

import logging
import time

import psycopg2
from confluent_kafka import Consumer

logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(20)

consumer_configuration = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'consumer1',
    'group.id': 'demo',
    'auto.offset.reset': 'earliest'
}

pg_config = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'port': '5432'
}

consumer = Consumer(consumer_configuration)
logging.info(f"Starting consumer with {consumer_configuration}")

try:
    conn = psycopg2.connect(**pg_config)
    cursor = conn.cursor()
    logging.info("Connected to PostgreSQL database")
    
    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kafka_messages (
            id SERIAL PRIMARY KEY,
            topic VARCHAR(255),
            partition INTEGER,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
except Exception as e:
    logging.error(f"Error connecting to PostgreSQL: {e}")
    exit(1)

consumer.subscribe(['demo_topic'])
logging.info("Subscribed to demo_topic")

try:
    while True:
        msg = consumer.poll(1.0)
        time.sleep(2)

        if msg is None:
            continue
        if msg.error():
            logging.error(f"Consumer error: {msg.error()}")
            continue
        message = msg.value().decode('utf-8')
        logging.info("decoded event")
        logging.info(f"Received message from topic => {msg.topic()}, partition => {msg.partition()}")
        
        try:
            cursor.execute("""
                INSERT INTO kafka_messages (topic, partition, message)
                VALUES (%s, %s, %s)
            """, (msg.topic(), msg.partition(), message))
            conn.commit()
            logging.info("Message written to PostgreSQL")
        except Exception as e:
            logging.error(f"Error writing to PostgreSQL: {e}")
            conn.rollback()

            