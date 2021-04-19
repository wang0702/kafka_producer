from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('my_topic', group_id='group2', bootstrap_servers=['localhost:9092'])
for msg in consumer:
    print("receive, key: {}, value: {}".format(
        msg.key.decode(),
        msg.value.decode()
    )
    )
