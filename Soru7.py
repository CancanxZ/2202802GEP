# What is the 10001st prime number?

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
    i = 0
    sayi = 2
    while True:
        if Asalmi(sayi):
            i += 1
            if i == 10001:
                return sayi
        sayi += 1  # çift sayılari skip

print(cevap())