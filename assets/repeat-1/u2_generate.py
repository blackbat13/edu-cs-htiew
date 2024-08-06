from random import randint


with open("u2.txt", "w") as file:
    for _ in range(100):
        print("".join([str(randint(0, 1)) for _ in range(1, randint(5, 10))]), file=file)

with open("u2_test.txt", "w") as file:
    for _ in range(10):
        print("".join([str(randint(0, 1)) for _ in range(1, randint(5, 10))]), file=file)