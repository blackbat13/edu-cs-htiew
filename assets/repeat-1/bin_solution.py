with open("long_bin.txt") as file:
    bin_num = file.read().strip()

current_digit = ""
current_length = 0
current_start = 0
max_length = 0
max_start = 0
max_digit = ""

for i, digit in enumerate(bin_num):
    if digit == current_digit:
        current_length += 1
    else:
        current_digit = digit
        current_length = 1
        current_start = i

    if current_length > max_length:
        max_length = current_length
        max_start = current_start
        max_digit = current_digit

print("Długość:", max_length)
print("Początek:", max_start + 1)
print("Koniec:", max_start + max_length)
print("Znak:", max_digit)