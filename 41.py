primes = []

for i in range(1, 100):
    for j in range(2, i):  # i == 9
        if i % j == 0:
            break
    else:  # zamani ke for break naseh ejra mishe
        primes.append(i)

print(primes)
