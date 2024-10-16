#1
def is_year_leap(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
  yr = test_data[i]
  print(yr,"->",end="")
  result = is_year_leap(yr)
  if result == test_results[i]:
      print("OK")
  else:
      print("Failed")

#2
# def is_year_leap(year):
#     if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#         return True
#     else:
#         return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987, 2024, 2100]
test_months = [2, 2, 1, 11, 2, 2]
test_results = [28, 29, 31, 30, 29, 28]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


#3
# def is_year_leap(year):
#     if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#         return True
#     else:
#         return False
#
# def days_in_month(year, month):
#     if month < 1 or month > 12:
#         return None
#
#     days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     if month == 2:
#         if is_year_leap(year):
#             return 29
#         else:
#             return 28
#
#     return days_in_months[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None

    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)

    total_days += day
    return total_days

print(day_of_year(2000, 12, 31))


#4
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


#5
def liters_100km_to_miles_gallon(liters):
    miles_per_km = 1 / 1.609344
    gallons_per_liter = 1 / 3.785411784
    return (100 * miles_per_km) / (liters * gallons_per_liter)

def miles_gallon_to_liters_100km(miles):
    km_per_mile = 1.609344
    liters_per_gallon = 3.785411784
    return (100 * liters_per_gallon) / (miles * km_per_mile)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


#6
def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 1, 2))
print(is_a_triangle(7, 10, 5))
print(is_a_triangle(10, 1, 1))

#7
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(6, 8, 10))
print(is_a_right_triangle(5, 5, 5))
print(is_a_right_triangle(1, 2, 3))







