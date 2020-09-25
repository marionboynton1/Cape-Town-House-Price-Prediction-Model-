from bs4 import BeautifulSoup
import requests
import csv
import time

df = open('p24_houses.csv','w')
csv_writer = csv.writer(df)
csv_writer.writerow(['page', 'price', 'location', 'address', 'desc', 'bedrooms', 'bathrooms', 'garages', 'size'])

page_list = list(range(1,20))

for i, n in enumerate(page_list):
    src = requests.get(f"https://www.property24.com/for-sale/alias/cape-town-city/19/western-cape/9/p{n}?PropertyCategory=House%2cApartmentOrFlat%2cTownhouse").text
    #time.sleep(20)
    page = BeautifulSoup(src, 'lxml')
    #results = page.find('div', class_ = 'p24_results')

    all_info= page.find_all(['span', 'div'], class_ = 'p24_content')
    #all_prices = page.find_all(['div', 'span'], class_ = 'p24_price')

    for value in all_info:
        try:
            price = value.find(['div', 'span'], class_='p24_price').text
        except Exception as no_price:
            price = None

        try:
            location = value.find(['div', 'span'], class_='p24_location').text
        except Exception as no_location:
            location = None

        try:
            address = value.find(['div', 'span'], class_='p24_address').text
        except Exception as no_location:
            address = None

        try:
            desc = value.find(['div', 'span'], class_=['p24_description', 'p24_title']).text
        except Exception as no_price:
            desc = None

        try:
            bedrooms = value.find(['div', 'span'], {'class': 'p24_featureDetails', 'title': 'Bedrooms'}).text
        except Exception as no_bedrooms:
            bedrooms = None

        try:
            bathrooms = value.find(['div', 'span'], {'class': 'p24_featureDetails', 'title': 'Bathrooms'}).text
            #bathrooms = value.find('div', class_='p24_icons').find_all(['div', 'span'], {'class': 'p24_featureDetails', 'title': 'Bathrooms'}).text
        except Exception as no_bathrooms:
            bathrooms = None

        try:
            #garages = value.find('div', class_='p24_icons').find(['svg'], class_='p24_garageIcon').find_next_sibling
            garages = value.find(['div', 'span'], {'class': 'p24_featureDetails', 'title': 'Parking Spaces'}).text
        except:
            garages = None

        try:
            size = value.find(['div', 'span'], {'class': ['p24_size', 'p24_featureDetails'], 'title': ['Erf Size', 'Floor Size']}).text
        except:
            size = None

        print(n, price, location, address, desc, bedrooms, bathrooms, garages, size)
        csv_writer.writerow([n, price, location, address, desc, bedrooms, bathrooms, garages, size])

df.close()
