from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Price(Base):
    __tablename__ = "price"
    id = Column(Integer, primary_key=True)
    value = Column(String(100), nullable=False)


class Apartments(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True)
    url = Column(String(150), nullable=False)
    img_src = Column(String(150), nullable=True)
    price_id = Column(ForeignKey(Price.id))
    price = relationship(Price)
    city = Column(String(50), nullable=False)
    time = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=False)
    bedrooms = Column(String(100), nullable=False)
