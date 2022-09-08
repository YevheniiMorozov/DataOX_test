from spider import get_data
from add_value_to_db import add_value
from sheets import add_value_to_sheets as sh


def main():

    print("Start application")

    data = get_data()
    prices, apartments = add_value(data)
    sh(prices, apartments)


if __name__ == '__main__':
    main()
