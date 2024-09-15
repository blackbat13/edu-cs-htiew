from random import randint

with open("points.txt", "w") as file:
    for i in range(1000):
        print(randint(1, 100), randint(1, 100), file=file)

with open("points_test.txt", "w") as file:
    for i in range(100):
        print(randint(1, 10), randint(1, 10), file=file)
