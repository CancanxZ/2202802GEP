# Find the sum of all the primes below two million.

def Asalmi(n):
    i = 2
    if n <= 1: #1 e küçük veya eşit ise asal olamaz
        return False
    while i * i <= n:
        if n % i == 0: #asal kontrolu
            return False
        i += 1
    return True

def cevap():
    toplam = 0
    sayi = 2
    while True:
        if Asalmi(sayi):
            if sayi >= 2000000: # 2 milyondan fazla ise return
                return toplam
            else:
                toplam += sayi # asal ise toplama ekle
        sayi += 1  # çift sayılari skip

print(cevap())