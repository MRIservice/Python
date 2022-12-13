#!/usr/bin/python3

print("\nFIZZ BUZZ\n")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FIZZ_BUZZ")
    elif num % 3 == 0:
        print("FIZZ")
    elif num % 5 == 0:
        print("BUZZ")
    else:
        print(num)
