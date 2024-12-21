from random import randint

digit_text_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digit_dict = {str(digit): digit_text for digit, digit_text in enumerate(digit_text_list)}

with open("spell_num.txt", "w") as file:
    for _ in range(100):
        num_str = str(randint(1, 10000))
        spelled_num = " ".join([digit_dict[digit] for digit in num_str])
        print(len(num_str), spelled_num, file=file)

with open("spell_num_test.txt", "w") as file:
    for _ in range(10):
        num_str = str(randint(1, 10000))
        spelled_num = " ".join([digit_dict[digit] for digit in num_str])
        print(len(num_str), spelled_num, file=file)