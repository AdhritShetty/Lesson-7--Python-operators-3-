print("There are ten ASCII values here. If you type the letters next to this respectively, it will give you the numerical value.")
user_input = str(input("Enter the value: "))

if user_input == 'A':
    print(65)
elif user_input == 'B':
    print(66)
elif user_input == 'C':
    print(67)
elif user_input == 'a':
    print(97)
elif user_input == 'b':
    print(98)
elif user_input == 'c':
    print(99)
elif user_input == 'H':
    print(72)
elif user_input == 'd':
    print(100)
elif user_input == 'e':
    print(101)
elif user_input == 'f':
    print(102)
else:
    print("Please enter one of these letters: A, B, C, a, b, c, H, d, e, f")