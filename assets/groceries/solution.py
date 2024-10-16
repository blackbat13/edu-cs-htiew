def transform(line):
    name, quantity, price = line.split()
    return (name, int(quantity), float(price))

def exercise1():
    with open(filename) as file:
        data = [transform(line) for line in file]

    result = 0

    for name, quantity, price in data:
        result += quantity * price

    print(f"{result:.2f}")

def is_prime(n):
    if n < 2:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True

def exercise2():
    with open(filename) as file:
        data = [transform(line) for line in file]

    result = 0

    for name, quantity, price in data:
        if is_prime(len(name)):
            result += quantity * price * 0.5
        else:
            result += quantity * price

    print(f"{result:.2f}")

def exercise3():
    with open(filename) as file:
        data = [transform(line) for line in file]

    quantity_sum = 0
    price_sum = 0

    for name, quantity, price in data:
        quantity_sum += quantity
        price_sum += price * quantity

    print(f"{price_sum / quantity_sum:.2f}")

def exercise4():
    with open(filename) as file:
        data = [transform(line) for line in file]

    groceries_dict = dict()

    for name, quantity, price in data:
        if name in groceries_dict:
            groceries_dict[name] += quantity
        else:
            groceries_dict[name] = quantity

    for name in sorted(groceries_dict):
        print(f"{name}: {groceries_dict[name]}")

def exercise5():
    with open(filename) as file:
        data = [transform(line) for line in file]

    groceries_dict = dict()

    for name, quantity, price in data:
        if name in groceries_dict:
            groceries_dict[name][0] += quantity
            groceries_dict[name][1] += price * quantity
        else:
            groceries_dict[name] = [quantity, price * quantity]

    for name in sorted(groceries_dict):
        print(f"{name}: {groceries_dict[name][1] / groceries_dict[name][0]:.2f}")

def exercise6():
    with open(filename) as file:
        data = [transform(line) for line in file]

    groceries_dict = dict()

    for name, quantity, price in data:
        if name in groceries_dict:
            groceries_dict[name][0] = min(price, groceries_dict[name][0])
            groceries_dict[name][1] = max(price, groceries_dict[name][1])
        else:
            groceries_dict[name] = [price, price]

    dif_list = [
        groceries_dict[name][1] - groceries_dict[name][0] for name in groceries_dict
    ]
    max_dif = max(dif_list)

    for name in sorted(groceries_dict):
        if groceries_dict[name][1] - groceries_dict[name][0] == max_dif:
            print(
                f"{name}: min: {groceries_dict[name][0]}, max: {groceries_dict[name][1]}"
            )

def exercise7():
    with open(filename) as file:
        data = [transform(line) for line in file]

    groceries_dict = dict()

    for name, quantity, price in data:
        if name in groceries_dict:
            groceries_dict[name].append(price)
        else:
            groceries_dict[name] = [price]

    for name in sorted(groceries_dict):
        prices = sorted(groceries_dict[name])
        print(f"{name}: {', '.join(map(str, prices))}")

def exercise8():
    with open(filename) as file:
        data = [transform(line) for line in file]

    groceries_dict = dict()
    result = 0

    for name, quantity, price in data:
        if name not in groceries_dict:
            groceries_dict[name] = 0

        if groceries_dict[name] + quantity <= 100:
            result += quantity * price
            groceries_dict[name] += quantity
        else:
            result += (100 - groceries_dict[name]) * price
            groceries_dict[name] = 100

    print(f"{result:.2f}")

filename = "groceries.txt"

for i in range(1, 9):
    print(f"Zadanie {i}:")
    exec(f"exercise{i}()")
    print()
