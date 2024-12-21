from faker import Faker
fake = Faker()
Faker.seed(0)

with open('names.txt', 'w') as f:
    for _ in range(100):
        print(fake.first_name(), file=f)

with open('names_test.txt', 'w') as f:
    for _ in range(10):
        print(fake.first_name(), file=f)