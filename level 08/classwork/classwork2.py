"""2) მომხმარებელს input-ის საშვალებით შემოტანინეთ ორი რიცხვი number1 და number2 შემდეგ კი დაბეჭდეთ მათი ჯამი. ასევე შექმენით level-ის ცვლადი რომელშიც მომხამრებელს შემოაყვანინებთ მათ ამჟამინდელ level-ს, შეეცადეთ level-ის მნიშვნელობას დაუმატოთ ერთი და ისე დაბეჭდოთ. მიღებული შედეგებით გამოიტანეთ დასკვნა და დაწერეთ კომენტარებით"""



num1 = input("choose number between 1-5:  ")
num2 = input("choose number between 5-10:  ")
print (num1 + " " + num2)


level = input("what is your level:  ")
print (int(level) + 1)