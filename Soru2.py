#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a, b = 0, 1
toplam = 0
#4 milyondan a 4 milyondan küçük olduğu sürece devam etmesi için while ekledim
while a <= 4000000:
    #a çift sayıysa toplama ekledim
    if a % 2 == 0:
        toplam += a
    #a ve b'nin yeni değerlerini atadım
    c = a + b
    a = b
    b = c

print(toplam)