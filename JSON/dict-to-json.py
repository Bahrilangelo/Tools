import json

# Dönüştürmek istediğimiz sözlük
sozluk = {
    "ad": "John Doe",
    "yas": 30,
    "meslek": "Mühendis",
    "email": "john@example.com"
}

# Sözlüğü JSON formatına dönüştürme
json_veri = json.dumps(sozluk)

# JSON formatındaki veriyi yazdırma
print(json_veri)
