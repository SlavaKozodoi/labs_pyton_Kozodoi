#1
n = int(input("Введіть значення n:"))
print(n >= 100)

#2
a = 5
b = 4
if(a>b):
    print(a,"більше")
else:
    print(b,"більше")

#3
inp = input("3:")
if(inp == "Spathiphyllum"):
    print("Yes - Spathiphyllum is the best plant ever!")
elif(inp == "spathiphyllum"):
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ",inp,"!")

#4
income = float(input("Enter the annual income: "))

if (income <= 85528):
    tax = 0.18 * income - 556.02
else:
    tax = 14839.02 + 0.32 * (income - 85528)
tax = round(tax)
print("The tax is:", tax, "thalers")

#5
year = int(input("Enter a year: "))
if(year >= 1582):
    if((year % 4 != 0) or (year % 400 != 0)):
        print(year, "Common year")
    elif(year % 100 != 0):
        print(year, "Leap year")
    else:
        print(year, "Leap year")
else:
    print(year, "Not within the Gregorian calendar period.")

#6
secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
enterWord = ""
while(enterWord != secret_number):
    enterWord = int(input("Enter a number: "))
    print("Ха-ха! Ви застрягли у моїй петлі!")
else:
    print("Молодець, магле! Тепер ти вільний")

#7
import time

for it in range(0,5):
    print(it+1,"Mississippi")
    time.sleep(1)

#8
while True:
    if(input("8 Input a word ")=="chupacabra"):
        break
print("You've successfully left the loop.")

#9
user_word = input("Введіть слово: ")
user_word = user_word.upper()
vowels = "AEIOU"

for letter in user_word:
    if letter in vowels:
        continue
    print(letter)

#10
word_without_vowels = ""
user_word = input("Введіть слово: ")
user_word = user_word.upper()
vowels = "AEIOU"

for letter in user_word:
    if letter in vowels:
        continue
    word_without_vowels += letter

print("Слово без голосних:", word_without_vowels)

#11
blocks = int(input("Введіть кількість блоків: "))
height = 0
required_blocks = 1

while blocks >= required_blocks:
    blocks -= required_blocks
    height += 1
    required_blocks += 1
print("Максимальна висота піраміди:", height)

#12
c0 = int(input("Введіть натуральне число: "))
steps = 0

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1

print(c0)
print("Кількість кроків до досягнення 1:", steps)













