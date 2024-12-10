import  requests
import bs4

r = requests.get("https://www.oreilly.co.jp/ebook/")

soup = bs4.BeautifulSoup(r.text, "html.parser")

# print(soup)

table = soup.find("table")

# print(table.prettify())

book_title = table.findAll("td")

# print(book_title)

for i in book_title:
    print(i.text)