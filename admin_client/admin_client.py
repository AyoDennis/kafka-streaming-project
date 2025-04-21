from confluent_kafka.admin import AdminClient, NewTopic

a = AdminClient({'bootstrap.servers': 'localhost:9092'})

new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in ["my_topic", "my_topic2"]]

fs = a.create_topics(new_topics)


