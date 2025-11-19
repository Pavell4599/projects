def is_devide_by_three(a):
    return (a%3 == 0)


nums = [24, 65, 23, -32, 75]
result = list(map(is_devide_by_three, nums))


print(result)


def my_func(a, b):
    return a * b


nums1 = [6, 7, 8, 9, 10]
nums2 = [1, 2, 3, 4, 5]

nums_multiply = list(map(my_func, nums1, nums2))

print(nums_multiply)