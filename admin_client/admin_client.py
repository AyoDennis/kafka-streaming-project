from confluent_kafka.admin import AdminClient, NewTopic

a = AdminClient({'bootstrap.servers': 'localhost:9092'})

