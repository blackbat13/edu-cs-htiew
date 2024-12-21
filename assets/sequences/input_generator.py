from random import randint

with open("sequences.txt", "w") as file:
    for i in range(10):
        lst = [randint(1, 1000) for _ in range(randint(100, 500))]
        print(len(lst), *lst, file=file)

with open("sequences_test.txt", "w") as file:
    for i in range(10):
        lst = [randint(1, 1000) for _ in range(randint(10, 50))]
        print(len(lst), *lst, file=file)
