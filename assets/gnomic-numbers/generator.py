from random import randint


with open("gnomiczne_przyklad.txt", "w") as file:
    for _ in range(10):
        print(bin(randint(100, 1000))[2:], file=file)

with open("gnomiczne.txt", "w") as file:
    for _ in range(100):
        print(bin(randint(10000000000, 10000000000000))[2:], file=file)