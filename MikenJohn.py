x = int(input("Введите минимальную сумму (X): "))
a = int(input("Введите сумму, которая есть у Майкла (A): "))
b = int(input("Введите сумму, которая есть у Ивана (B): "))

# Все условия
if a >= x and b >= x:
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)