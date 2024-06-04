# Find the largest palindrome made from the product of two 3-digit numbers

def PalindromMu(sayi):
    # palindrom kontrol fonksiyonu
    return str(sayi) == str(sayi)[::-1]

def PalindromBulmaFonksiyon():
    #max palindromu bulma fonksiyonu
    max_palindrom = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            # Gereksiz hesaplamaları engellemek için j'yi i'den başlat
            carpim = i * j
            if PalindromMu(carpim) and carpim > max_palindrom:
                max_palindrom = carpim
    return max_palindrom

en_buyuk_palindrom = PalindromBulmaFonksiyon()
print(en_buyuk_palindrom)