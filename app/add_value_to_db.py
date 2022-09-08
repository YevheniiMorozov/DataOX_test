from database import engine, Session
from models import Base, Apartments, Price


def add_value(data):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    prices = set([element["price"] for element in data])
    prices_list = [Price(value=el) for el in list(prices)]

    with engine.connect() as connection:
        with Session(bind=connection) as session:
            session.add_all(prices_list)
            session.commit()
            print("Prises added")

            prices_dict = {el.value: el.id for el in session.query(Price).all()}

    apartments = []
    for element in data:
        price = element["price"]
        apartment = element["apartments"]

        apartments.append(Apartments(
            url=apartment["url"],
            img_src=apartment['img_src'],
            description=apartment['description'],
            price_id=prices_dict[price],
            time=apartment["time"],
            bedrooms=apartment['bedrooms'],
            city=apartment['city']
        ))
    with engine.connect() as connection:
        with Session(bind=connection) as session:
            session.add_all(apartments)
            session.commit()
            print("Apartments added")

            apartments = session.query(Apartments).all()
            prices_dict = {el.id: el.value for el in session.query(Price).all()}

    return prices_dict, apartments
