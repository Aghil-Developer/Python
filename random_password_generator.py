import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+','/','=','_','?','<',',','.','|','[',']','{','}',':',';']


password = ""
passwordList = []

numberOfLetters = int(input("Enter the number of letters: "))
numberOfNumbers = int(input("Enter the number of numbers: "))
numberOfSymbols = int(input("Enter the number of symbols: "))

for i in range(0,numberOfLetters):
    chars = random.choice(letters)
    password += chars
    passwordList.append(chars)

for i in range(0,numberOfNumbers):
    chars = random.choice(numbers)
    password += chars
    passwordList.append(chars)

for i in range(0,numberOfSymbols):
    chars = random.choice(symbols)
    password += chars
    passwordList.append(chars)

random.shuffle(passwordList)
print("The random password mixed is ","".join(passwordList))

print("The random password without mixed is ",password)
