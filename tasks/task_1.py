def middle(numbers) -> float:
    return round(sum(numbers) / len(numbers), 3)


print(middle([1, 2, 3, 9, 0, 3, 6]))
help(middle)