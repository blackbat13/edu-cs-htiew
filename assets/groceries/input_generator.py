from random import choice, randint, random

groceries = [
    "apples", "bananas", "carrots", "dates", "eggs", "flour", "garlic",
    "honey", "iceberg", "jam", "kale", "lemons", "milk", "nuts", "oranges",
    "pasta", "quinoa", "rice", "spinach", "tomatoes", "yogurt", "zucchini",
    "bread", "chicken", "onions", "potatoes", "cheese", "butter", "salmon",
    "avocado", "cucumber", "grapes", "olives", "peppers", "yams"
]

with open('groceries.txt', 'w') as f:
    for _ in range(1000):
        print(f"{choice(groceries)} {randint(1, 100)} {random() * 10 + 0.01:.2f}", file=f)

with open('groceries_test.txt', 'w') as f:
    for _ in range(100):
        print(f"{choice(groceries)} {randint(1, 100)} {random() * 10 + 0.01:.2f}", file=f)