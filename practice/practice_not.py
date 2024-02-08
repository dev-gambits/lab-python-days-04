# Verificar si el valor de stock está fuera del rango entre 100 y 1000
stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print('Compare: not (stock >= 100 and stock <= 1000)')
print(not (stock >= 100 and stock <= 1000))

print()

print('Compare: stock >= 100 and stock <= 1000')
print(stock >= 100 and stock <= 1000)

## OUTPUT TERMINAL, INPUT NUMER IS 555.
# Ingrese el numero de stock => 555
# Compare: not (stock >= 100 and stock <= 1000)
# False

# Compare: stock >= 100 and stock <= 1000
# True