# number = int(input('Enter any number : '))
# divisors = [i for i in range(1, number + 1) if number % i == 0]

# if len(divisors) == 2:
#     print(number, 'is prime')
# else:
#     print(number, 'is composite')


number = int(input('Enter any number : '))
divisors = [i for i in range(1, number + 1) if number % i == 0]
print(divisors)

if divisors == [1, number]:
    print(number, 'is prime')
else:
    print(number, 'is composite')
