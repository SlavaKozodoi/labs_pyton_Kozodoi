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









