def exercise1():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        if name[0] == "B":
            count += 1

    print(count)

def exercise2():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        if name[-1] == "a":
            count += 1

    print(count)

def exercise3():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        if name[0] in "AEYUIO":
            count += 1

    print(count)

def exercise4():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        if name[0] not in "AEYUIO" and name[-1] in "aeyuio":
            count += 1

    print(count)

def exercise5():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        for i in range(1, len(name) - 1):
            if name[i] == "e":
                count += 1
                break

    print(count)

def exercise6():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    for name in names_list:
        if name.count("a") + name.count("A") > 1:
            print(name)

def exercise7():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    for name in names_list:
        if name.count("a") + name.count("A") == 0:
            print(name)

def exercise8():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    for name in names_list:
        for i in range(1, len(name)):
            if name[i] == name[i - 1]:
                print(name)
                break

def count_vowels(text):
    vowels = "aeiouy"
    count = 0
    for character in text:
        if character in vowels:
            count += 1

    return count

def exercise9():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    vowels_counters = [count_vowels(name) for name in names_list]
    max_vowels = max(vowels_counters)
    max_vowels_names = [
        names_list[i]
        for i in range(len(names_list))
        if vowels_counters[i] == max_vowels
    ]

    print("\n".join(sorted(max_vowels_names)))

def exercise10():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    names_lengths = [len(name) for name in names_list]
    min_length = min(names_lengths)
    max_length = max(names_lengths)

    min_names = [name for name in names_list if len(name) == min_length]
    max_names = [name for name in names_list if len(name) == max_length]

    print("Najkrótsze imiona:")
    print("Długość:", min_length)
    print("Imiona:", ", ".join(min_names))
    print()
    print("Najdłuższe imiona:")
    print("Długość:", max_length)
    print("Imiona:", ", ".join(max_names))

def exercise11():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    names_set = set(names_list)

    print(len(names_set))

def exercise12():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    names_set = set(names_list)
    unique_names = [name for name in names_set if names_list.count(name) == 1]

    print("\n".join(sorted(unique_names)))

def exercise13():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    names_set = set(names_list)
    names_dict = {name: names_list.count(name) for name in names_set}
    max_count = max(names_dict.values())
    most_common_names = [
        name for name, count in names_dict.items() if count == max_count
    ]

    print("\n".join(most_common_names))

def exercise14():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    result = [name for name in names_list if len(name) == len(set(name.lower()))]
    print("\n".join(sorted(result)))

def sum_ascii(name):
    return sum(ord(char) for char in name)

def exercise15():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    ascii_sums_list = [sum_ascii(name) for name in names_list]
    min_sum = min(ascii_sums_list)
    max_sum = max(ascii_sums_list)
    min_sum_names = [
        name for name, sum in zip(names_list, ascii_sums_list) if sum == min_sum
    ]
    max_sum_names = [
        name for name, sum in zip(names_list, ascii_sums_list) if sum == max_sum
    ]

    print(f"Najmniejsza suma ascii: {min_sum}")
    print("Imiona:", "\n".join(min_sum_names))
    print()
    print(f"Największa suma ascii: {max_sum}")
    print("Imiona:", "\n".join(max_sum_names))

def exercise16():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    max_length = 1
    max_start = 0
    max_end = 0
    current_length = 1
    current_start = 0
    current_end = 0

    for i in range(1, len(names_list)):
        if names_list[i] > names_list[i - 1]:
            current_length += 1
            current_end = i
        else:
            current_length = 1
            current_start = i
            current_end = i

        if current_length > max_length:
            max_length = current_length
            max_start = current_start
            max_end = current_end

    max_names = names_list[max_start : max_end + 1]
    print(f"Liczba imion: {max_length}")
    print("Początek sekwencji:", max_start + 1)
    print("Koniec sekwencji:", max_end + 1)
    print(f"Najdłuższa sekwencja rosnących imion:")
    print("\n".join(max_names))

file_name = "names.txt"

for i in range(1, 17):
    print(f"Zadanie {i}:")
    exec(f"exercise{i}()")
    print()
