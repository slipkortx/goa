total = 0
count = 0

while True:
    number = int(input("Enter a number (or -1 to stop): "))
    
    if number == -1:
        break
    
    total += number
    count += 1

if count > 0:
    average = total / count
    print()
else:
    print()