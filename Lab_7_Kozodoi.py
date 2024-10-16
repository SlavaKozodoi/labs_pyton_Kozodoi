#1
numbers = [10, 25, 8, 17, 3, 45, 19, 7]

numbers_tuple = tuple(numbers)

n = int(input("Введіть число n: "))

result = [num for num in numbers_tuple if num < n]

print(f"Числа менші за {n}: {result}")


#2
my_tuple = ("яблуко", "банан", "апельсин")

result = ", ".join(my_tuple)

print(result)



#3
library = {
    "1984": {"author": "Джордж Оруелл", "year": 1949, "pages": 328},
    "To Kill a Mockingbird": {"author": "Харпер Лі", "year": 1960, "pages": 281},
    "The Great Gatsby": {"author": "Френсіс Скотт Фіцджеральд", "year": 1925, "pages": 180},
    "Moby Dick": {"author": "Герман Мелвілл", "year": 1851, "pages": 635},
    "Pride and Prejudice": {"author": "Джейн Остін", "year": 1813, "pages": 432}
}

book_title = input("Введіть назву книги: ")

if book_title in library:
    book_info = library[book_title]
    print(f"Назва книги: {book_title}")
    print(f"Автор: {book_info['author']}")
    print(f"Рік видання: {book_info['year']}")
    print(f"Кількість сторінок: {book_info['pages']}")
else:
    print("Книга не знайдена в бібліотеці.")





#4
students = {
    "Іваненко": ("21", "KN-101", 4.5),
    "Петренко": ("22", "KN-102", 3.8),
    "Сидоренко": ("20", "KN-101", 4.0),
    "Коваленко": ("23", "KN-103", 4.8),
    "Шевченко": ("22", "KN-102", 3.5)
}

surname = input("Введіть прізвище студента: ")

if surname in students:
    student_info = students[surname]
    print(f"Прізвище студента: {surname}")
    print(f"Вік: {student_info[0]}")
    print(f"Група: {student_info[1]}")
    print(f"Середній бал: {student_info[2]}")
else:
    print("Студента не знайдено в базі даних.")


#5
phone_book = {
    "Іван Петров": ["+380501234567", "+380501234568"],
    "Оксана Джуга": ["+380501234569"],
    "Андрій Коваленко": ["+380501234570", "+380501234571", "+380501234572"],
}

def add_phone_number(name, phone_number):
    if name in phone_book:
        phone_book[name].append(phone_number)
        print(f"Номер телефону {phone_number} додано до контакту {name}.")
    else:
        print(f"Контакт {name} не знайдено в телефонній книзі.")

add_phone_number("Оксана Джуга", "+380501234573")
add_phone_number("Петро Іванов", "+380501234574")  # Контакт не існує

print("\nСписок номерів телефонів для всіх контактів:")
for contact, numbers in phone_book.items():
    print(f"{contact}: {', '.join(numbers)}")



