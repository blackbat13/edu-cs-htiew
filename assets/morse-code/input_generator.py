import morse_talk as mtalk
from faker import Faker
from random import shuffle


fake = Faker()

with open("morse_alphabet.txt", "w") as file:
    for letter_ascii in range(ord("A"), ord("Z") + 1):
        letter = chr(letter_ascii)
        morse_code = mtalk.encode(letter)
        print(letter, morse_code, file=file)
    
    for digit_ascii in range(ord("0"), ord("9") + 1):
        digit = chr(digit_ascii)
        morse_code = mtalk.encode(digit)
        print(digit, morse_code, file=file)

palindromes = ['KAYAK', 'DEIFIED', 'ROTATOR', 'REPAPER', 'DEED', 'PEEP', 'WOW', 'NOON', 'CIVIC', 'RACECAR']

with open("morse.txt", "w") as file_enc, open("morse_decoded.txt", "w") as file_dec:
    words = [fake.word().upper() for _ in range(90)] + palindromes
    shuffle(words)
    for word in words:
        print(word, file=file_dec)
        print(mtalk.encode(word).replace("   ", " "), file=file_enc)

with open("morse_test.txt", "w") as file_enc, open("morse_test_decoded.txt", "w") as file_dec:
    words = [fake.word().upper() for _ in range(7)] + ["LEVEL", "MOM", "MMO"]
    shuffle(words)
    for word in words:
        print(word, file=file_dec)
        print(mtalk.encode(word).replace("   ", " "), file=file_enc)