#1
def ispalindrom(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        print("It's a palindrom")
    else:
        print("It's not a palindrom")

text = input("Введіть текст:")
ispalindrom(text)

text = input("Введіть текст:")
ispalindrom(text)

#2

text1 = input("Введіть перше слово:")
text2 = input("Введіть друге слово:")

text1 = list(text1.replace(" ", "").lower())
text2 = list(text2.replace(" ", "").lower())

if sorted(text1) == sorted(text2):
    print("Анаграми")
else:
    print("Не анаграми")


#3
date = input("Введіть дату народження у форматі YYYYMMDD:")

while True:
    sum = 0
    for simbol in date:
        sum += int(simbol)

    date = str(sum)

    if len(date) == 1:
        break

print(sum)


#1

def is_word_hidden(word, text):
    index = 0
    for char in word:
        index = text.find(char, index)
        if index == -1:
            return "No"
        index += 1
    return "Yes"

print(is_word_hidden("dog", "vcxzxduybfdsobywuefgas"))
print(is_word_hidden("dog", "vcxzxdcybfdstbywuefsas"))


#4
while True:
    try:
        number = int(input(" Введіть ціле число: "))
        print(number/2)
        break
    except:
        print("Введене значення не є допустимим числом. Повторіть спробу...")



#2

print(is_word_hidden("dog", "vcxzxduybfdsobywuefgas"))
print(is_word_hidden("dog", "vcxzxdcybfdstbywuefsas"))
print(is_word_hidden("dog", 12345))
print(is_word_hidden("dog"))
def is_word_hidden(word, text):
    try:
        index = 0
        for char in word:
            index = text.find(char, index)
            if index == -1:
                return "No"
            index += 1
        return "Yes"
    except TypeError:
        return "Error: Обидва аргументи повинні бути рядками."
    except Exception as e:
        return f"Unexpected error: {e}"


#3
def get_integer_in_range(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
            else:
                return value
        except ValueError:
            print("Error: wrong input")

result = get_integer_in_range("Please enter an integer: ", 10, 20)
print(f"You entered: {result}")
