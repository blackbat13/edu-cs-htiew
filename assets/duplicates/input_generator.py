from random import randint

with open("duplicates.txt", "w") as file:
    for i in range(100):
        print(randint(1, 100), file=file)

with open("duplicates_test.txt", "w") as file:
    for i in range(10):
        print(randint(1, 10), file=file)