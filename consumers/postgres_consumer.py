from dotenv import load_dotenv

load_dotenv()

import logging
import time

import psycopg2
from confluent_kafka import Consumer

logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(20)
