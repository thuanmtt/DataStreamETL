import yaml
from confluent_kafka import Consumer


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


def init_kafka_consumer(config):
    consumer_config = {
        "bootstrap.servers": config["kafka"]["bootstrap_servers"],
        "group.id": config["kafka"]["group_id"],
        "auto.offset.reset": "earliest",
    }
    consumer = Consumer(consumer_config)
    consumer.subscribe([config["kafka"]["topic"]])
    return consumer
