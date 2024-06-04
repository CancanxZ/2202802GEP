# There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.

def PisagorUclusuBulmaFonksiyonu():
    for a in range(1, 1000):
        for b in range(a, 1000): # b, a dan büyük olacağı için kontrole a dan başladık
            c = 1000 - a - b
            if c > 0:
                if a**2 + b**2 == c**2: # pisagor kontrol
                    return a, b, c

a, b, c = PisagorUclusuBulmaFonksiyonu()
print(a*b*c)