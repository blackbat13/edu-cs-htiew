from itertools import accumulate
from random import randint, choices, shuffle


triangle_numbers = list(accumulate(range(1, 50001)))

triangle_numbers_big = list(filter(lambda x: x > 10**9, triangle_numbers))

triangle_numbers_small = list(filter(lambda x: x < 10**3, triangle_numbers))

print(triangle_numbers_big, len(triangle_numbers_big))
print(triangle_numbers_small, len(triangle_numbers_small))

data_example = [randint(1, 1000) for _ in range(8)] + choices(triangle_numbers_small, k=2)
data = [randint(10**9, 2 * (10**9)) for _ in range(90)] + choices(triangle_numbers_big, k=10)
shuffle(data)
shuffle(data_example)
with open("trojkatne_przyklad.txt", "w") as file:
    print(*data_example, sep="\n", end="", file=file)

with open("trojkatne.txt", "w") as file:
    print(*data, sep="\n", end="", file=file)