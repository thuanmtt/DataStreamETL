import json

import yaml
from confluent_kafka import Producer


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


def init_kafka_producer(config):
    producer_config = {"bootstrap.servers": config["kafka"]["bootstrap_servers"]}
    return Producer(producer_config)


def delivery_report(err, msg):
    """Callback được gọi khi message được gửi hoặc gặp lỗi"""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def produce_message(producer, topic, message):
    """Phát một message tới Kafka topic"""
    producer.produce(
        topic, json.dumps(message).encode("utf-8"), callback=delivery_report
    )
    producer.flush()
