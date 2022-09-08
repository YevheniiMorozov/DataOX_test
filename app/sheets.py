import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = [
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open('apartments').sheet1


def add_value_to_sheets(prices, apart):
    sheet.clear()
    headers = ["url", "img_src", "city", "time", "description", 'bedrooms', "price"]
    sheet.insert_row(headers, 1)
    for index, element in enumerate(apart, 2):
        values = [element.url, element.img_src, element.city, element.time,
                  element.description, element.bedrooms, prices[element.price_id]]

        sheet.insert_row(values, index)
        # quota limit value is 60
        time.sleep(1)
