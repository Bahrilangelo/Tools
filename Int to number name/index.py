import inflect
ans = 2
# inflect kütüphanesini kullanarak sayıyı metinsel ifadeye çevirme
p = inflect.engine()
for i in range(1,1001):
    for k in p.number_to_words(i):
        if k != ' ' and k != '-':
            ans += 1

print(ans)  # Çıktı: 'two'
