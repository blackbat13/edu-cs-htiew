from random import randint


with open("long_bin.txt", "w") as file:
    print("1" + "".join([str(randint(0, 1)) for _ in range(999)]), file=file)

with open("short_bin.txt", "w") as file:
    print("1" + "".join([str(randint(0, 1)) for _ in range(99)]), file=file)