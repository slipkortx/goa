even_count = 0
odd_count = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break
    
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print()