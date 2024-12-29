def find_numbers():
    results = []
    for number in range(100, 1000):
        # Разбиваем число на цифры
        a = number // 100  # Сотни
        b = (number // 10) % 10  # Десятки
        c = number % 10  # Единицы

        # Проверяем условие
        if a + b + c == a * b * c:
            results.append(number)

    return results


# Выводим результат
numbers = find_numbers()
print("Числа, удовлетворяющие условию:")
print(numbers)
