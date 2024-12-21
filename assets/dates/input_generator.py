from random import randint, shuffle

def generate_date():
    day = randint(1, 31)
    month = randint(1, 12)
    year = randint(100, 3000)
    date = [day, month, year]
    shuffle(date)
    return date

with open("dates.txt", "w") as file:
    for i in range(1000):
        date = generate_date()
        print(*date, file=file)

with open("dates_test.txt", "w") as file:
    for i in range(100):
        date = generate_date()
        print(*date, file=file)