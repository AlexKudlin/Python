number = int(input("Введите число: "))

a = number // 10000
b = (number // 1000) % 10
c = (number // 100) % 10
d = (number // 10) % 10
e = number % 10

result = ((d ** e) * c) / (a - b)

print('Итоговый результат: ', result)