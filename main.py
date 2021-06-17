from bs4 import BeautifulSoup
import lxml
import requests
import csv


url1 = "https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/?PAGEN_1="
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}

count = 1

with open("casio_watch.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(("Model", "Image", "Price", "Link"))

while count <= 5:

    url = url1 + str(count)
    print('*****************' * 5)
    print(url)


    req = requests.get(url=url, headers=headers)

    with open(f'index{count}.html', 'w') as file:
        file.write(req.text)


    # with open(f'index_all.html', 'r') as file:
    #     src = file.read()

    with open(f'index{count}.html', 'r') as file:
        src = file.read()

    count += 1

    soup = BeautifulSoup(src, 'lxml')


    product_item = soup.find_all(class_='product-item carousel-item')

    for item in product_item:
        link = item.find(class_='product-item__link')
        product_link = "https://shop.casio.ru" + link.get('href')
        print(product_link)

        product_model = item.find(class_='product-item__articul').text
        print("Model: " + product_model.strip())

        picture = item.find('picture').find('img').get("data-src")
        if picture==None:
            picture = item.find('picture').find('img').get("src")
        picture_link = "https://shop.casio.ru" + picture
        print('Mini image link: ' + picture_link)

        price = item.find(class_='product-item__price').find(class_="rouble").next_element.next_element.next_element.strip()
        print("Price: " + price + " rub")

        print('----------------' * 5)

        with open("casio_watch.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow((product_model, picture_link, price, product_link))











