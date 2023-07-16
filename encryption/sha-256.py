import hashlib

def sha256_sifrele(metin):
    # Metni SHA-256 algoritmasıyla şifrele
    sha256_objesi = hashlib.sha256()
    sha256_objesi.update(metin.encode('utf-8'))
    sifreli_metin = sha256_objesi.hexdigest()
    return sifreli_metin

# Şifrelenecek metni kullanıcıdan alın
metin = input("Şifrelenecek metni girin: ")

# Metni SHA-256 ile şifrele
sifreli_metin = sha256_sifrele(metin)

# Şifreli metni ekrana yazdır
print("Şifreli metin:", sifreli_metin)
