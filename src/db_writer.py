from sqlalchemy.exc import SQLAlchemyError

from models.db_model import YourDataModel


def write_to_db(session, data):
    new_record = YourDataModel(**data)
    try:
        session.add(new_record)
        session.commit()
    except SQLAlchemyError as e:
        print(f"Error writing to DB: {e}")
        session.rollback()
