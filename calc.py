# a = int(input("Введіть число a: "))
# action = input("Введіть дію ")
# b = int(input("Введіть число b: "))

# if (action == "+" or action == " +" or action == "+ " or action == " + "):
#   print("Сума чисел рівна " + str(a + b))
# elif (action == "-" or action == " -" or action == "- " or action == " - "):
#    print("Різниця чисел рівна " + str(a - b))
# elif (action == "/" or action == " /" or action == "/ " or action == " / "):
#   print("Частка чисел рівна " + str(a / b))
# elif (action == "*" or action == " *" or action == "*" or action == " * "):
#   print("Добуток чисел рівна " + str(a * b))
# else:
#   print("Неправильна дія")

# # rez = a if (a > b) else b

# rez = 0
# if (a>b):
#   rez = a
# else:
#   rez = b

# print(rez)

n = input('Введіть число = ')
while type(n) != int:
    try:
        n = int(n)
        print("парне число") if (n % 2 == 0) else print("Непарне число")
                 
    except ValueError:
        print("Неправильне ввели число")
        n = input('Введіть ціле число = ')
