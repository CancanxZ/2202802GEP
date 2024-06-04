
# What is the largest prime factor of the number 600851475143?
sayi = 600851475143

#böleni bulmak için 1 parametre alan bir fonksiyon oluşturdum
def EnBuyukBolen(n):
    #i'yi en küçük asal sayıya setledim
    i = 2
    
    #i'nin karesi n den küçük olduğu sürece n'nin içinde minimum 2 farklı asal sayı olduğu için i kare n'den küçük olduğu sürece while loop'u çalışıyor
    while i * i <= n:
        #i n'nin bir böleni olup olmadığını kontrol ediyoruz. böleni değilse 1 ekliyoruz
        if n % i:
            i += 1
        #i n'nin bir böleni ise n'yi i'ye bölüyoruz.
        else:
            n /= i
    #n en büyük asal sayı değerine ulaştığında while loop'undan çıkıyor ve n'yi döndürüyoruz.
    return n

cevap = EnBuyukBolen(sayi)

print(cevap)