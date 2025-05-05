import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
STORE_ID = "clickclucksho-20" #Your Amazons Associate ID

def generate_affiliate_link(product_url):
    if "tag=" in product_url:
        return product_url
    joiner = "&" if "?" in product_url else "?"
    return f"{product_url}{joiner}tag={STORE_ID}"

def send_to_discord(message):
    data={"content":message} 
    response=requests.post(WEBHOOK_URL,json=data)
    if response.status_code == 204: 

        print("send_to_Discord!")

    else:

        print("Failed to send:{response.status_code}-{response.text}")

if __name__=="__main__":
    product_link = input("Paste Amazon product URL:").strip()
    affiliate_link = generate_affiliate_link(product_link)
    send_to_discord(f"**Deal of the day**{affiliate_link}")

