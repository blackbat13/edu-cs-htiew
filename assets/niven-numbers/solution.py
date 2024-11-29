def is_niven(n):
    return n % (sum(map(int, str(n)))) == 0


with open("niven.txt") as file:
    numbers = [int(line) for line in file]

niven_numbers = [k for k in numbers if is_niven(k)]

print(*niven_numbers, sep="\n")