number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive and even.")
    else:
        print("Positive and odd.")
elif number < 0:
    print("Negative.")
else:
    print("Zero.")