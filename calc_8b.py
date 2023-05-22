a = float(input("Введіть число a: "))
action = input("Введіть дію: ")
b = float(input("Введіть число b: "))
print()

# if (action == "+" or action == " +" or action == "+ " or action == " + "):
#   print("Сума чисел рівна " + str(a + b))
# elif (action == "-" or action == " -" or action == "- " or action == " - "):
#   print("Різниця чисел рівна " + str(a - b))
# elif (action == "*" or action == " *" or action == "* " or action == " * "):
#   print("Добуток чисел рівний " + str(a * b))
# elif (action == "/" or action == " /" or action == "/ " or action == " / "):
#   print("Частка чисел рівна " + str(a / b))
# else:
#   print('не правильна дія')

# # " +" "+ " " + "
# # " -" "- " " - "
# # " *" "* " " * "
# # " /" "/ " " / "

# max = 0
# if (a > b):
#     max = a
# else:
#     max = b

max = a if (a > b) else b   

print(max)
# str(a + b) if (action == "+") else "Не правильна дія"

rez = ("Сума чисел дорівнює " + str(a + b)) if (action == "+") else "Не дія додавання"
print(rez)