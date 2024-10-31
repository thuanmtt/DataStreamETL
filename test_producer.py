from src.kafka_producer import init_kafka_producer, load_config, produce_message

if __name__ == "__main__":
    config = load_config()
    producer = init_kafka_producer(config)

    # Tạo message mẫu
    sample_message = {
        "field1": "Sample data",
        "field2": 123.45,
    }

    # Phát message vào Kafka
    produce_message(producer, config["kafka"]["topic"], sample_message)
