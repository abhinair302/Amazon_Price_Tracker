from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1" #You can add your own product url
smtp_address=os.environ.get("SMTP_ADDRESS")
email_address=os.environ.get("EMAIL_ADDRESS")
email_password=os.environ.get("EMAIL_PASSWORD")


response=requests.get(url,headers={"Accept-Language":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"})

soup=BeautifulSoup(response.text,"html.parser")

price_whole=soup.find("span", {"class": "a-offscreen"}).string.strip()
price=float(price_whole.split("$")[1])
print(price)

target_price=100 #You can Add your own target price.
item_name=soup.find(id="productTitle").string.strip()
print(item_name)


if price<target_price:
    message=f"{item_name} is now ${price}\n{url}"


    with smtplib.SMTP(smtp_address,port=587) as connection:
        connection.starttls()
        connection.login(user=email_address,password=email_password)
        connection.sendmail(from_addr=email_address,
                            to_addrs=email_address,
                            msg=message.encode('utf-8'))

    print("Succesfully Send an Email")






