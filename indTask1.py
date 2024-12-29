def age_phrase(n):
    if 11 <= n % 100 <= 19:
        word = "лет"
    else:
        last_digit = n % 10
        if last_digit == 1:
            word = "год"
        elif 2 <= last_digit <= 4:
            word = "года"
        else:
            word = "лет"

    print(f"Мне {n} {word}")


# Пример использования
n = int(input("Введите натуральное число меньше 100: "))
if 1 <= n < 100:
    age_phrase(n)
else:
    print("Число должно быть от 1 до 99!")
