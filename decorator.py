def hey():
    name = input("Как вас зовут? ")
    return f"Привет, {name}"

def dekor(function):  # Принимает функцию
    def better_function():
        print("Сейчас будет запрошена личная информация!")
        name = function()
        print("Тайна раскрыта: вас зовут " + name) 
        return name

    return better_function

hello = dekor(hey)
hello()