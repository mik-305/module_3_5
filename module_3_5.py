def get_multiplied_digits(number):
    global rezult
    str_number = str(number)  # Преобразование числа в стоку
    if str_number[0] != '0':  # Пропускаем нули
        first = int(str_number[0])  # Первое число
        print('---Перемножаемые числа------', first)
        if len(str_number) > 1:
            rezult = first * get_multiplied_digits(int(str_number[1:]))
        else:
            rezult = first
        return rezult
    else:
        return rezult


get_multiplied_digits(40203)
print('Результат -', rezult)
print()
get_multiplied_digits(1)
print('Результат =', rezult)
print()
get_multiplied_digits(7007)
print('Результат =', rezult)
