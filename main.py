from models.db_model import init_db
from src.data_cleaner import clean_data
from src.db_writer import write_to_db
from src.kafka_comsumer import consume_data
from utils.kafka_connection import init_kafka_consumer, load_config

if __name__ == "__main__":
    config = load_config()
    consumer = init_kafka_consumer(config)
    session = init_db(config["postgres"])

    for raw_data in consume_data(consumer):
        cleaned_data = clean_data(raw_data)
        write_to_db(session, cleaned_data)
