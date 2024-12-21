def exercise1():
    digit_text_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digit_dict = {digit_text: str(digit) for digit, digit_text in enumerate(digit_text_list)}
    with open(file_name) as file:
        for line in file:
            line_list = line.split()
            length = int(line_list[0])

file_name = "spell_num_test.txt"

for i in range(1, 2):
    print(f"Zadanie {i}:")
    exec(f"exercise{i}()")
    print()
