import os
import sqlalchemy
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from db import PhoneNumber, UserData
from sqlalchemy import func

load_dotenv()


engine = sqlalchemy.create_engine(
    os.getenv("SQLALCHEMY_DATABASE_URI")
)  # connect to server
session = Session(engine)
phone_number = session.query(PhoneNumber)
print(f"Общее количесвто записей: {phone_number.count()}")

count_unique_phone = func.count(PhoneNumber.id).label("count")
phone_number_not_unique_list = (
    session.query(PhoneNumber.phone, count_unique_phone)
    .group_by(PhoneNumber.phone)
    .having(count_unique_phone > 1)
)
print(f"Кол-во не уникальных номеров телефонов: {phone_number_not_unique_list.count()}")
for phone_number in phone_number_not_unique_list:
    print(f"{phone_number[0]}")

print("Статистика по людям:")
user_data_born_to_year = (
    session.query(func.count(UserData.id), func.year(UserData.birth_day))
    .group_by(func.year(UserData.birth_day))
    .order_by(func.year(UserData.birth_day).asc())
)
for born_to_year in user_data_born_to_year:
    print(f"Год: {born_to_year[1]}. Рождено: {born_to_year[0]}")

count = func.count(UserData.id).label("count")
namesakes = (
    session.query(UserData.last_name, count)
    .group_by(UserData.last_name)
    .having(count > 1)
)
print(f"Кол-во однофамильцев: {namesakes.count()}")
