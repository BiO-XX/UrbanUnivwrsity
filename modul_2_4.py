numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in numbers:
    is_prime = True
    for j in range(2, i):
        while j * j <= i:
            if i % j == 0:
                is_prime = 0
                break
            j += 1
    if i == 1:
        continue
    elif is_prime == 1:
        prime.append(i)
    elif is_prime == 0:
        not_prime.append(i)

print(prime)
print(not_prime)
