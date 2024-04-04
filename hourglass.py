def hourglass():
    size = input("Введите размер песочных часов: ")
    x = int(size)
    for i in range(x, 0, -1):  # Верхняя часть песочных часов
        chast1 = (" " * (x - i) + "*" * (2 * i - 1))
        print(chast1)
    for i in range(2, x + 1):  # Нижняя часть песочных часов
        chast2 = (" " * (x - i) + "*" * (2 * i - 1)) 
        print(chast2)
    full = chast1, chast2
    return full

def dekor(function):  # Принимает функцию
    def better_function():
        print("Смотрите, как я могу!")
        full = function()
        print("Правда, красиво?") 
        return full

    return better_function

hello = dekor(hourglass)
hello()
          