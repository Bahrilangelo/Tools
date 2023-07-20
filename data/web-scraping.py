import requests
from bs4 import BeautifulSoup

def scrape_books():
    # Web sitesine HTTP GET isteği gönderiyoruz.
    response = requests.get("http://books.toscrape.com/")
    
    # İstek başarılı mı diye kontrol ediyoruz.
    if response.status_code == 200:
        # İçeriği BeautifulSoup kütüphanesi ile işleyelim.
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Kitapları içeren ana bölümü bulalım.
        books_section = soup.find("ol", class_="row")
        
        if books_section:
            # Her bir kitabın detaylarını alalım.
            books = books_section.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
            
            # Kitapların bilgilerini saklayacağımız bir liste oluşturalım.
            book_list = []
            
            # Her kitap için bilgileri çekelim.
            for book in books:
                title = book.h3.a["title"]
                price = book.select(".price_color")[0].text
                author = book.select(".author")[0].text
                
                # Kitap bilgilerini bir sözlük olarak liste içine ekleyelim.
                book_info = {
                    "title": title,
                    "price": price,
                    "author": author
                }
                book_list.append(book_info)
            
            return book_list
        else:
            print("Kitaplar bulunamadı.")
            return None
    else:
        print("İstek başarısız oldu. Durum kodu:", response.status_code)
        return None

# Kitapları çekelim ve ekrana yazdıralım.
books = scrape_books()
if books:
    for book in books:
        print("Kitap Adı:", book["title"])
        print("Yazar:", book["author"])
        print("Fiyat:", book["price"])
        print("------------------------")
