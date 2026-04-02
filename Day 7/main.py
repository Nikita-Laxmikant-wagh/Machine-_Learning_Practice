import requests
from bs4 import BeautifulSoup
import os

os.makedirs("Scraped_Data", exist_ok=True)


page_count = 1

while True:
    url = f"https://quotes.toscrape.com/page/{page_count}/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    if not quotes:
        print("No more quotes found. Stopping.")
        break

    file_path = f"Scraped_Data/quote_page_{page_count}.html"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"Page {page_count} scraped successfully.")
    page_count += 1



with open("Scraped_Data/quote_page_1.html", "r", encoding="utf-8") as file:
    content = file.read()
    soup = BeautifulSoup(content, "html.parser")
    all_quotes = soup.select("div.quote")

for quote in all_quotes:
    all_tags = []
    Life_quote = []

    for tag in quote.select(".tags .tag"):
        all_tags.append(tag.get_text())
    
    if "life" in all_tags:
        text = quote.select_one("span.text").get_text()
        author = quote.select_one("small.author").get_text()
        Life_quote.append([text, author])

print(Life_quote)


    
    