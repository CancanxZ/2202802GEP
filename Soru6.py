# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# karelerin toplami hesabi
kareleritoplami = sum(i ** 2 for i in range(1, 101))

# toplamlarin karesi hesabi
toplamlarikaresi = sum(range(1, 101)) ** 2

# fark hesabi
fark = toplamlarikaresi - kareleritoplami

print(fark)