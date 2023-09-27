from sqlalchemy import Column, Integer, ForeignKey, BigInteger, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PhoneNumber(Base):
    __tablename__ = "phone_number"

    id = Column(Integer, primary_key=True)
    phone = Column(BigInteger, nullable=False)


class UserData(Base):
    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True)
    phone_number_id = Column(Integer, ForeignKey("phone_number.id"), nullable=False)
    phone_number = relationship("PhoneNumber")
    field1 = Column(String(255), nullable=True)
    field2 = Column(String(255), nullable=True)
    first_name = Column(String(255), nullable=True)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    field5 = Column(Integer, nullable=True)
    field6 = Column(String(255), nullable=True)
    field7 = Column(String(255), nullable=True)
    birth_day = Column(DateTime, nullable=True)
    field9 = Column(Integer, nullable=True)
    field10 = Column(Integer, nullable=True)
    field11 = Column(String(255), nullable=True)
    field12 = Column(String(255), nullable=True)
    field13 = Column(Integer, nullable=True)
