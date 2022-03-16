def get_number(x, y):
    if (x % 2 == 0) and (y % 2 == 0):
        return min(x, y)
    else:
        return max(x, y)


# Después de la función siempre deja dos espacios antes de un comentario
# console input
a = int(input("Ingrese un número: "))
b = int(input("ingrese un número: "))

r = get_number(a, b)
print(r)
