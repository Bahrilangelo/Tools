import numpy as np
import matplotlib as plt

# 1000 adet rasgele Tails ve Heads ifadesi oluşturma
data = np.random.choice(['Tails', 'Heads'], size=1000)

# Tails ve Heads sayılarını hesapla
tails_count = np.count_nonzero(data == 'Tails')
heads_count = np.count_nonzero(data == 'Heads')

# Etiketler ve veriler
labels = ['Tails', 'Heads']
values = [tails_count, heads_count]

# Pasta grafiği oluştur
plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Tails vs Heads Dağılımı')
plt.axis('equal')

# Grafiği göster
plt.show()
