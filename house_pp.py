from bs4 import BeautifulSoup
import requests
import csv
import time

df = open('pp_tableblou.csv','w')
csv_writer = csv.writer(df)
csv_writer.writerow(['page', 'price', 'location', 'address', 'suburb', 'desc', 'type', 'bedrooms', 'bathrooms', 'garages'])

page_list = list(range(1,145))

#areas = ['atlantic-seaboard/1683', 'bellville/737', 'brackenfell/883', 'buh-rein/2292', 'cape-flats/56', 'cape-town-city-bowl/59', 'durbanville/739', 'goodwood/740', 'hout-bay/1684', 'kraaifontein/885', 'kuilsriver/738', 'matroosfontein/3055', 'melkbosstrand/61', 'milnerton/1399', 'parow/2497', 'peninsula-false-bay/57', 'southern-suburbs/58', 'tableview-and-blouberg/60' ]

for i, n in enumerate(page_list):
    src = requests.get(f"https://www.privateproperty.co.za/for-sale/western-cape/cape-town/tableview-and-blouberg/60?pt=5,2,10&page={n}").text
    page = BeautifulSoup(src, 'lxml')

    all_info= page.find_all(['span', 'div'], class_ = 'infoHolder')

    for value in all_info:

        try:
            price = value.find(['div', 'span'], class_='priceDescription').text
        except Exception as no_price:
            price = None

        location = 'tableview and blouberg'

        try:
            address = value.find(['div', 'span'], class_='address').text
        except Exception as no_location:
            address = None

        try:
            suburb = value.find(['div', 'span'], class_='suburb').text
        except Exception as no_location:
            suburb = None

        try:
            desc = value.find(['div', 'span'], class_=['uspsString']).text
        except Exception as no_price:
            desc = None

        try:
            type = value.find(['div', 'span'], class_=['propertyType']).text
        except Exception as no_price:
            type = None

        try:
            bedrooms = value.find(['div', 'span'], {'class': 'icon bedroom'}).find_previous_sibling(['div', 'span'], class_=['number']).text
        except Exception as no_bedrooms:
            bedrooms = None

        try:
            bathrooms = value.find(['div', 'span'], {'class': 'icon bathroom'}).find_previous_sibling(['div', 'span'], class_=['number']).text
        except Exception as no_bathrooms
            bathrooms = None

        try:
            garages = value.find(['div', 'span'], {'class': 'icon garage'}).find_previous_sibling(['div', 'span'], class_=['number']).text
        except Exception as no_garages:
            garages = None

        csv_writer.writerow([n, price, location, address, suburb, desc, type, bedrooms, bathrooms, garages])

df.close()
