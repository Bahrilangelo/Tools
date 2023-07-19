from Crypto.PublicKey import RSA

# İki anahtar oluşturun: bir açık anahtar ve bir özel anahtar.
public_key, private_key = RSA.generate(2048)

# Açık anahtarı başka bir kullanıcıyla paylaşın.
with open("public_key.pem", "wb") as f:
    f.write(public_key.save_pkcs1())

# Özel anahtarı kendinizle saklayın.
with open("private_key.pem", "wb") as f:
    f.write(private_key.save_pkcs1())

# Açık anahtarı kullanarak bir mesajı şifreleyin.
message = "Hello, world!"
encrypted_message = public_key.encrypt(message.encode("utf-8"))

# Özel anahtarı kullanarak şifrelenmiş mesajı çözmek için.
decrypted_message = private_key.decrypt(encrypted_message).decode("utf-8")

print(decrypted_message)
