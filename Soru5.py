# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import gcd

def EKOKFonsiyon(a, b):
    #iki sayının ekok hesaplama fonsiyonu
    return a * b // gcd(a, b)

def ArrayEKOKFonksiyon(sayilar):
    #bir array den ekok hesabı fonksiyonu
    cevap = sayilar[0]
    for sayi in sayilar[1:]:
        cevap = EKOKFonsiyon(cevap, sayi)
    return cevap

# array
sayilar = range(1, 21)

# 1 den 20 ye ekok hesapları
ekokcevap = ArrayEKOKFonksiyon(sayilar)

print(ekokcevap)
