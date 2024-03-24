def summa(x, y):
    return x + y

def ras(x, y):
    return x - y

def umn(x, y):
    return x * y

def delen(x, y):
    return x / y

def fly(x, y):
    return x**y

def kor(x):
    return x**0.5

def proz(x,y):
    return x * y / 100

print("Выберете операцию:")
print("1. Сложить")
print("2. Вычесть")
print("3. Умножить")
print("4. Деление")
print("5. Возведение в степень")
print("6. Корень")
print("7. Найти процент от числа")
print("8. Выход")

while True:
    choice = input("Выберете действие(1/2/3/4/5/6/7/8): ")
    if choice in ("1", "2", "3", "4", "5"):
        num1 = float(input("Введите число: "))
        num2 = float(input("Введите число: "))       
        if choice == "1":
            print(num1, "+", num2, "=", summa(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", ras(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", umn(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", delen(num1, num2))
        elif choice == "5":
            print(num1, "**", num2, "=", fly(num1, num2))
    elif choice == "6":
        num1 = float(input("Введите число: "))
        print(num1, "=", kor(num1))
    elif choice == "7":
        num1 = float(input("Введите число, у которого нужно найти процент: "))
        num2 = float(input("Введите число процентов: "))
        print(num1, "*", num2, "/", "100", "=", proz(num1, num2))
    elif choice == "8":
        break
    else:
      print("Неизвестная команда.")




