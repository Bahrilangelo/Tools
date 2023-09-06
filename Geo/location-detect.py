import requests

def get_location_by_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    return data

ip = ""  # Your Ip Adress
location_data = get_location_by_ip(ip)
print("Konum Bilgisi:", location_data)
