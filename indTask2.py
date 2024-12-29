def japanese_calendar(year):
    # Названия животных в подцикле
    animals = [
        "мышь", "корова", "тигр", "заяц", "дракон",
        "змея", "лошадь", "овца", "обезьяна", "курица",
        "собака", "свинья"
    ]
    # Названия цветов
    colors = ["зеленый", "красный", "желтый", "белый", "черный"]

    # Начальный год цикла
    base_year = 1984

    # Вычисляем смещение от начала цикла
    offset = (year - base_year) % 60

    # Определяем животное и цвет
    animal = animals[offset % 12]
    color = colors[(offset // 12) % 5]

    return f"{year} - год {color} {animal}"

# Пример использования
year = int(input("Введите год: "))
if year >= 1984:
    print(japanese_calendar(year))
else:
    print("Год должен быть не меньше 1984!")
