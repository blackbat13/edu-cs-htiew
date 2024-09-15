from collections import Counter

def exercise1():
    with open(file_name) as file:
        dates = [list(map(int, line.split())) for line in file.read().strip().split("\n")]

    result = 0
    for date in dates:
        year = max(date)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            result += 1

    print(result)


def exercise2():
    with open(file_name) as file:
        dates = [list(map(int, line.split())) for line in file.read().strip().split("\n")]

    result = 0
    for date in dates:
        year = max(date)
        date.remove(year)
        day = max(date)
        if day > 12:
            result += 1

    print(result)

def exercise3():
    with open(file_name) as file:
        dates = [list(map(int, line.split())) for line in file.read().strip().split("\n")]

    result = 0
    ordered_dates = []
    for date in dates:
        month, day, year = sorted(date)
        ordered_dates.append((year, month, day))

    ordered_dates.sort()
    print("Najstarsza:", ordered_dates[0])
    print("Najmłodsza:", ordered_dates[-1])

def exercise4():
    with open(file_name) as file:
        dates = [list(map(int, line.split())) for line in file.read().strip().split("\n")]

    result = 0
    months = [min(date) for date in dates]
    months_count = Counter(months)
    print(months_count)

def exercise5():
    with open(file_name) as file:
        dates = [list(map(int, line.split())) for line in file.read().strip().split("\n")]

    result = 0
    years = [max(date) for date in dates]
    current_length = 1
    current_start_year = years[0]
    max_start_year = years[0]
    max_end_year = years[0]
    max_length = 1
    for i, year in enumerate(years[1:], 1):
        if year > years[i - 1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_start_year = current_start_year
                max_end_year = year
        else:
            current_start_year = year
            current_length = 1

    print("Długość:", max_length)
    print("Rok startowy:", max_start_year)
    print("Rok końcowy:", max_end_year)

def exercise6():
    with open(file_name) as file:
        dates = [list(map(int, line.split())) for line in file.read().strip().split("\n")]

    result = 0
    ordered_dates = []
    for date in dates:
        month, day, year = sorted(date)
        ordered_dates.append((year, month, day))

    result = 0
    for i, date1 in enumerate(ordered_dates):
        for date2 in ordered_dates[i + 1:]:
            year1, month1, day1 = date1
            year2, month2, day2 = date2
            if month1 + month2 <= 12 and day1 + day2 <= 31:
                result += 1

    print(result)

file_name = "dates.txt"

for i in range(1, 7):
    print(f"Zadanie {i}:")
    exec(f"exercise{i}()")
    print()
