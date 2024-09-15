from faker import Faker

fake = Faker()

for i in range(100):
    print(fake.file_path(depth=fake.random.randint(1, 10)))