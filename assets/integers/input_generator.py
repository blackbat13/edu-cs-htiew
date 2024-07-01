from random import randint

rand_num_set = set()

while len(rand_num_set) < 100:
    rand_num_set.add(randint(2, 200))

with open("integers.txt", "w") as file:
    for num in rand_num_set:
        print(num, file=file)

with open("integers_test.txt", "w") as file:
    for i, num in enumerate(rand_num_set):
        if i >= 10:
            break
        print(num, file=file)