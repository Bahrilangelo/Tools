import socket

def get_ip_address():
    try:
        # İnternet üzerinden bağlantı oluştur
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # Google DNS sunucusuna geçici bir bağlantı oluştur

        # Bağlantı yapıldığında yerel IP adresini al
        ip_address = sock.getsockname()[0]

        return ip_address
    except socket.error:
        return "IP adresi alınamadı"

ip = get_ip_address()
print("IP Adresi:", ip)
