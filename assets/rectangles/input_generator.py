from random import randint

n = 50

def generate_rectangle_coordinates():
    x1, y1 = randint(-n, n-1), randint(-n+1, n)
    x2, y2 = randint(x1 + 1, n), randint(-n, y1 - 1)
    
    return x1, y1, x2, y2


with open("rectangles.txt", "w") as file:
    for _ in range(100):
        x1, y1, x2, y2 = generate_rectangle_coordinates()
        print(f"{x1} {y1} {x2} {y2}", file=file)


with open("rectangles_test.txt", "w") as file:
    for _ in range(10):
        x1, y1, x2, y2 = generate_rectangle_coordinates()
        print(f"{x1} {y1} {x2} {y2}", file=file)
