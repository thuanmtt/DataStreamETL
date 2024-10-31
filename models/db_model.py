from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class YourDataModel(Base):
    __tablename__ = "your_data_table"
    id = Column(Integer, primary_key=True)
    data_field1 = Column(String)
    data_field2 = Column(Float)
    # Thêm các trường khác nếu cần


# Khởi tạo engine và session
def init_db(config):
    engine = create_engine(
        f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
