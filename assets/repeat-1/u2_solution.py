def u2_to_int(u2_num):
    first_digit = u2_num[0]
    if first_digit == "0":
        return int(u2_num, 2)
    return int(u2_num[1:], 2) - 2 ** (len(u2_num) - 1)


with open("u2.txt") as file:
    u2_numbers = file.read().strip().split()

u2_numbers.sort(key=lambda el: u2_to_int(el))

print(u2_numbers)
print(list(map(u2_to_int, u2_numbers)))

print("Minimum:", u2_numbers[0])
print("Maksimum:", u2_numbers[-1])