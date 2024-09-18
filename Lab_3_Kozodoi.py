#1
import math
x=0
mu = 0
sigma =1
result =(1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
print(result)

#2
john =3
marry =5
adam = 6
print(john, marry, adam,sep=",")
totalAple=john+marry+adam
print(totalAple)
print("Загальна кількість яблук:"+str(totalAple))

#3
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#4
x =1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3**x - 1
print(y)

#5
# this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
print("Goodbye")
a=3
print("Hours: ", a)
print("Seconds in Hours: ", a * seconds)


#6
a = 13.4
b = 4.5

print("addition"+str(a+b))
print("subtraction "+str(a-b))
print("multiplication "+str(a*b))
print("division "+str(a/b))
print("\nThat's all, folks!")

#7
x = float(input("Введіть значення x: "))
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("y =", y)

#8
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
inMins=hour*60+mins+dura
hour=(inMins//60)%24
mins=(inMins%60)
print(hour,mins,sep=":")
