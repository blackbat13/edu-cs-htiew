from faker import Faker
from random import choice

fake = Faker()

with open("visits.txt", "w") as file:
    print("Poczatek sesji;Koniec sesji;Adres strony;Adres IP", file=file)
    urls = [fake.domain_name() for _ in range(20)]
    for i in range(1000):
        start = fake.date_time()
        stop = fake.date_time()
        url = choice(urls)
        ip = fake.ipv4()
        print(f"{start};{stop};{url};{ip}", file=file)
