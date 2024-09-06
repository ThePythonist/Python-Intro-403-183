def show_divisors(x):
    return [i for i in range(1, x + 1) if x % i == 0]


# nums = [10, 8, 6, 15]

# without map
# for i in nums:
#     print((show_divisors(i)))

# with map
# print(list(map(show_divisors, nums)))
print(list(map(show_divisors, [int(input("Enter a number : ")) for i in range(3)])))

# ---------------------------------------------------------------

# def show_divisors(x):
#     return [i for i in range(1, x + 1) if x % i == 0]
#
#
# nums = [6, 28, 12]
# result = map(show_divisors, nums)
#
# # print(list(zip(nums,result)))
#
# for adad, shomarandeha in zip(nums, result):
#     print(adad, ":", shomarandeha)
