numero = int

for numero in range(1, 1001):
    if numero % 15 == 0:
        print("FIZZBUZZ")
    elif numero % 5 == 0:
        print("BUZZ")
    elif numero % 3 == 0:
        print("FIZZ")
    else:
        print(f"{numero}")
    