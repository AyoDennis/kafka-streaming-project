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
    'database': 'postgres',  # Change to your database name
    'user': 'postgres',     # Change to your username
    'password': 'postgres', # Change to your password
    'port': '5432'          # Change if your PostgreSQL uses a different port
}
