# Básico:imprime todos los números enteros del 0 al 150.

for x in range(0,150):
    print(x)

# Múltiplos de cinco:Imprime todos los múltiplos de 5 entre 5 y 1,000.

for x in range(5,1000):
    if x % 5==0:
        print(x)

# Contar, a la manera del Dojo:imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".

for x in range (1,100):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# Whoa. Es un gran idiota:agrega los enteros impares del 0 al 500,000, e imprime la suma final.
suma = 0
i = 0

for x in range (0,500000):
    if x % 2 != 0:
        print(x)
        suma = suma + x
        i = i + 1
print("la suma de los numeros impares entre 0 y 500000 = ",suma)

# Cuenta regresiva de a 4:imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

num = 2019
for x in range (1, num + 1, 4):
    print(num - x)

# Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.

lowNum = 2
hightNum = 9
mult = 3 

for x in range(lowNum,hightNum+1):
    if x % mult ==0:
        print(x)







