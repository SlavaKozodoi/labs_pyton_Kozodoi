
__counter = 0  

def suml(the_list):
    """Функція для обчислення суми елементів списку."""
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prodl(the_list):
    """Функція для обчислення добутку елементів списку."""
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

# Виконання тестів при запуску файлу безпосередньо
if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i + 1 for i in range(5)]
    print("Сума елементів:", suml(my_list) == 15)
    print("Добуток елементів:", prodl(my_list) == 120)