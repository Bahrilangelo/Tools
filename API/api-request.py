import json
import requests

headers = {"user-agent": "ravenfo", "Content-Type": "application/json"}
# user-agent ile sunucuya kendi tarayıcımızın adının “ravenfo” olduğunu ve alacağımız veri tipinin JSON formatında olduğu bilgisini özellikle ilettik.

istek = requests.get("https://api.github.com/", headers=headers)

# Get metodunun birden fazla ozelligi vardir
# url (zorunlu): İstek gönderilecek adres.
# params (isteğe bağlı): Gönderilen isteği özelleştirebilecek ifadeler.
# headers (isteğe bağlı): İsteğin nasıl yorumlanacağına dair sunucuya bilgi veren ifadeler.
# cookies (isteğe bağlı): İstemciye ait oturum (session) bilgilerini saklayan ifadeler.
# auth (isteğe bağlı): İstemciye ait kimlik bilgileri.
# timeout (isteğe bağlı): Gönderilen isteğin yanıtı için beklenecek saniye cinsinden süre.

parameters = {
    "market": "TR",
    "ids": "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B",
}

tr_song = requests.get("https://api.spotify.com/v1/tracks", params=parameters)

"""
Spotify API‘si ile milyonlarca şarkıya ait veriye erişme imkanınız var. 
Fakat araştırmanız gereği, sadece Türkiye’den yayınlanmış eserlerle ilgileniyorsunuz. 
Parametreler sayesinde ilgisiz diğer verileri de sorgulayıp, zaman ve güç israf etmek yerine sadece istediğiniz doğru veriye erişebilirsiniz.
"""

#Yandex
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
requests.get(url, params = {key=API_KEY})
 
#Zendesk
url = "https://your_subdomain.zendesk.com/api/v2/groups.json"
requests.get(url, auth=("username", "password"))

'''
Çoğu API kullanım öncesinde kimlik doğrulaması istemektedir.
API kimlik bilgilerini genelde API dokümanında belirtilen şekilde tamamlayıp, karşılığında bir API anahtarı (API key) elde ederiz. 
Bu API key ve servis tarafından istenen diğer bilgileri auth veya params argümanlarını kullanarak sunarız.
Hangi argümanı kullanacağımız ve nasıl giriş yapacağımız yine API dokümantasyonunda servis tarafından belirtilmiştir.
'''

# Yanit
istek = requests.get("https://api.github.com")
 
istek.status_code

# Yanit basligi (headers)
istek = requests.get("https://api.github.com")
istek.headers

# Icerik
istek = requests.get("https://api.github.com")
istek.json()