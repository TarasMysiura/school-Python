# Задача 1. На скільки років потрібно покласти в банк суму have, щоб отримати суму want,
# якщо банк нараховує 25% річних? Вивести на екран значення суми кожного року і загальну кількість років.

# have_0 = int(input("Введіть суму, яку ви маєте "))
# want = int(input("Введіть суму, якої хочете досягти "))
# v = int(input("Введіть відсоткову ставку "))

# have = have_0
# i = 0
# while (have <= want):
#     have = round((have + have * v / 100), 2)
#     print(have)
#     i += 1
# print(i)

# have = have_0
# arr = []
# while (have <= want):
#     have = round((have + have * v / 100), 2)
#     arr.append(have)
# print(arr)
# print(len(arr))


# Задача 3. В учнів було S грн. В школі проходить збір макулатури. Один чистий зошит коштує new грн,
# списаний зошит  коштує full грн. Складіть алгоритм, за яким можна визначити, скільки учні зможуть купити зошитів,
# якщо вони повертатимуть списані зошити й на отримані гроші купуватимуть чисті?


s = 100
new = 10
full = 2

s1 = 0
i = 0
while (s1 <= s):
    s1 = s1 + (new - full) * i
    # print(s1)
    i = i + 1
print(i)

# a = 0

# for a in range(1,10,4):
#     print(a)
# print()
# print(a)

# a = int(input("a = "))
# b = int(input("b = "))

# suma = 0
# j = 0
# for i in range(a,b):
#     suma += i  # suma = suma + i
#     j += 1
#     print("Suma = " + str(suma))
#     if (i == 4):
#         break
# print()
# print(j)
# print("Suma = " + str(suma))
# print("Avenge = " + str(suma / j))
