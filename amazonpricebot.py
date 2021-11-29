import requests
import lxml
from bs4 import BeautifulSoup

myemail = "anirudhaiml@gmail.com"
password = "anirudh@03042001"


url = "https://www.amazon.in/Pringles-Cream-Onion-Potato-Chips/dp/B084LGBN35/ref=sr_1_9?keywords=pringles&qid=1638172220&sr=8-9"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("₹")[1 ]
price_as_float = float(price_without_currency)
print(price_as_float)

""" with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=myemail, password=password)
    connection.sendmail(from_addr=myemail, to_addrs="anirudhvasudevan11@gmail.com", msg="Subject:the price is low now\n\n get it") """


import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "anirudhaiml@gmail.com"  # Enter your address
receiver_email = "anirudhaiml@gmail.com"  # Enter receiver address
password = "anirudh@03042001"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)