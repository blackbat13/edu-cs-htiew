def exercise1():
    pass


def exercise2():
    with open(file_name) as file:
        data = [line.split() for line in file.read().strip().split("\n")]

    result = 0
    for message in data:
        if message == message[::-1]:
            result += 1

    print(result)

def exercise3():
    with open(file_name) as file:
        data = [line.split() for line in file.read().strip().split("\n")]

    min_length = len(min(data, key= lambda el: len(el)))
    max_length = len(max(data, key= lambda el: len(el)))
    print("Najdłuższy:", max_length)
    print("Najkrótszy:", min_length)

def exercise4():
    with open(file_name) as file:
        data = [line.split() for line in file.read().strip().split("\n")]

    result = 0
    for i, message1 in enumerate(data):
        for message2 in data[i+1:]:
            if sorted(message1) == sorted(message2):
                result += 1

    print(result)


file_name = "morse.txt"

for i in range(1, 5):
    print(f"Zadanie {i}:")
    exec(f"exercise{i}()")
    print()
