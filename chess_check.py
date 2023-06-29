user_input = input()
letter = user_input[0]
number = int(user_input[1])
letter_interpretation = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
number_from_letter = int(letter_interpretation.get(letter))
if (number + number_from_letter) % 2 == 0:
    print("Black")
else:
    print("White")