import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import os

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
EXPECTED_PRICE = 20000
URL = "https://www.amazon.in/Gigabyte-GeForce-1660-SUPER-Graphics/dp/B093Z4TMHP/ref=sr_1_5?keywords=graphic+card&refinements=p_72%3A1318476031%2Cp_36%3A1318507031%2Cp_n_format_browse-bin%3A30678576031&rnid=30678571031&s=computers&sr=1-5"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, 'html.parser')
price = soup.select(".a-price .a-offscreen")[0].getText().strip()
price_float = float(price.replace(',', '').split('₹')[1])
product_name = soup.select("#productTitle")[0].getText().strip()
print(product_name)

if price_float <= EXPECTED_PRICE:
    message = f"Subject: Amazon Price Reduce Alert!\n\n{product_name} price has been dropped to Rs.{price_float}\nShop now: {URL}"
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(msg=message,
                            from_addr=EMAIL,
                            to_addrs=EMAIL)
