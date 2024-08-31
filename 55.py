# def is_prime(number):
#     # Comprehension
#     divisors = [i for i in range(1, number + 1) if number % i == 0]
#     print("prime") if len(divisors) == 2 else print("not prime")
#
#
# is_prime(int(input('Enter any number : ')))

def is_prime(number):
    # Comprehension
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return "prime" if len(divisors) == 2 else "not prime"


print(is_prime(int(input('Enter any number : '))))
