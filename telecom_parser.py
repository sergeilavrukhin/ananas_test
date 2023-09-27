from datetime import datetime
import os
import urllib.request
import sqlalchemy
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import re

from db import PhoneNumber, UserData

load_dotenv()


engine = sqlalchemy.create_engine(
    os.getenv("SQLALCHEMY_DATABASE_URI")
)  # connect to server
engine.execute("SET FOREIGN_KEY_CHECKS = 0;")
engine.execute("TRUNCATE TABLE user_data;")
engine.execute("TRUNCATE TABLE phone_number;")
engine.execute("SET FOREIGN_KEY_CHECKS = 1;")
session = Session(engine)
user_data_list = urllib.request.urlopen(
    "https://lk.globtelecom.ru/upload/test_prog1.csv"
).readlines()
for user_data in user_data_list:
    data = user_data.decode("windows-1251").split(";")
    phone = re.sub("[^0-9]", "", data[0])
    if len(phone) == 11:
        phone_number = PhoneNumber(phone=phone)
        session.add(phone_number)
        user_data = UserData(
            phone_number=phone_number,
            field1=data[1],
            field2=data[2],
            last_name=data[4].split(" ")[0],
            first_name=data[4].split(" ")[1],
            middle_name=data[4].split(" ")[2],
            field5=data[5],
            field6=data[6],
            field7=data[7],
            birth_day=datetime.strptime(data[8], "%d.%m.%Y"),
            field9=data[9],
            field10=data[10],
            field11=data[11],
            field12=data[12],
            field13=data[13],
        )
        session.add(user_data)
    else:
        print(f"Ошибочный номер: {phone}")
session.commit()
