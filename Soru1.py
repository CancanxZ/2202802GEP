#Find the sum of all the multiples of 3 or 5 below 1000.

toplam = 0
#1000'e kadar olan sayıları tek tek for loopunda çağırdım
for i in range(1000):
    #sayı 3'ün veya 5'in katı mı diye kontrol ettim
    if i % 5 == 0 or i % 3 == 0:
        #sayı 3'ün veya 5'in katı ise topladım
        toplam += i
print(toplam)