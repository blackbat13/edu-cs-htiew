def is_triangle_number(k):
    left = 1
    right = k
    while left <= right:
        middle = (left + right) // 2
        n_sum = ((1 + middle) * middle) // 2
        if n_sum == k:
            return True
        elif n_sum < k:
            left = middle + 1
        else:
            right = middle - 1

    return False

def is_triangle_number_linear(k):
    n = 1
    c_sum = 0
    while c_sum < k:
        c_sum += n
        n += 1

    return c_sum == k


with open("trojkatne_przyklad.txt") as file:
    numbers = [int(line) for line in file]

triangle_numbers = [k for k in numbers if is_triangle_number(k)]

print(*triangle_numbers, sep="\n")