from math import gcd

def exercise1():
    with open(file_name) as file:
        sequences = []
        for line in file:
            sequences.append(list(map(int, line.split()))[1:])

    for seq in sequences:
        print(sum(seq))

def exercise2():
    with open(file_name) as file:
        sequences = []
        for line in file:
            sequences.append(list(map(int, line.split()))[1:])

    for seq in sequences:
        print(f"Minimum: {min(seq)}, Maksimum: {max(seq)}")

def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True

def exercise3():
    with open(file_name) as file:
        sequences = []
        for line in file:
            sequences.append(list(map(int, line.split()))[1:])

    for seq in sequences:
        primes = []
        for num in seq:
            if is_prime(num):
                primes.append(num)

        print(f"Ile pierwszych: {len(primes)}, Liczby pierwsze: ", end="")
        print(*primes)

def exercise4():
    with open(file_name) as file:
        sequences = []
        for line in file:
            sequences.append(list(map(int, line.split()))[1:])

    for seq in sequences:
        current_length = max_length = 1
        current_start = max_start = 0
        for i in range(1, len(seq)):
            if seq[i] > seq[i - 1]:
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
                    max_start = current_start
            else:
                current_length = 1
                current_start = i

        print(f"Dlugosc: {max_length}, Sekwencja: ", end="")
        print(*seq[max_start : max_start + max_length])

def exercise5():
    with open(file_name) as file:
        sequences = []
        for line in file:
            sequences.append(list(map(int, line.split()))[1:])

    for seq in sequences:
        count = 0
        for i in range(len(seq)):
            for j in range(i + 1, len(seq)):
                if gcd(seq[i], seq[j]) == 1:
                    count += 1

        print(count)

file_name = "sequences.txt"

for i in range(1, 6):
    print(f"Zadanie {i}:")
    exec(f"exercise{i}()")
    print()
