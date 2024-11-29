from itertools import accumulate
from random import randint, choices, shuffle


def is_niven(n):
    return n % (sum(map(int, str(n)))) == 0


niven_numbers = list(filter(lambda x: is_niven(x), range(1, 10**6)))

niven_numbers_big = list(filter(lambda x: x > 10**5, niven_numbers))

niven_numbers_small = list(filter(lambda x: x < 10**3, niven_numbers))

# print(niven_numbers_big, len(niven_numbers_big))
# print(niven_numbers_small, len(niven_numbers_small))

data_example = [randint(1, 1000) for _ in range(8)] + choices(niven_numbers_small, k=2)
data = [randint(10**5, (10**6)) for _ in range(90)] + choices(niven_numbers_big, k=10)
shuffle(data)
shuffle(data_example)

with open("niven_przyklad.txt", "w") as file:
    print(*data_example, sep="\n", end="", file=file)

with open("niven.txt", "w") as file:
    print(*data, sep="\n", end="", file=file)