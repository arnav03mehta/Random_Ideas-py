import requests
from bs4 import BeautifulSoup
from funlib import cut
import smtplib
import time

url = 'https://www.amazon.in/Mi-Smart-Band-4-Black/dp/B07WLL998K/ref=sr_1_1?crid=2J9HW9HL0DW2P&keywords=mi+band+4+watch&qid=1574690656&sprefix=mi+%2Caps%2C305&sr=8-1'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}


def price_check():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id='priceblock_ourprice').get_text()
    conv_price = ''
    for i in range(len(price)):
        if price[i] == '₹':
            continue
        elif price[i] == " ":
            continue
        elif price[i] == ",":
            continue
        elif price[i] == ".":
            break
        else:
            conv_price += price[i]

    conv_price = int(conv_price)

    if conv_price < 2500:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls
    server.ehlo()

    server.login('arnavskate@gmail.com', 'password')
    subject = 'Hey! price fell down!! '
    body = ' Check it out now ! (link): https://www.amazon.in/gp/product/B07WLL998K/ref=ox_sc_act_title_1?smid=A14CZOWI0VEHLG&psc=1'
    msg = f"Subject : {subject} \n \n {body} "

    server.sendmail(
        'arnavskate@gmail.com',
        'arnav2003meht@gmail.com',
        msg
    )
    print('hey! message sent!!!!!!!')

    server.quit()


while (True):
    price_check()
    time.sleep(60 * 60)
