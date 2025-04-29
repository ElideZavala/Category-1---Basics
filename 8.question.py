# Print the following pattern

"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

def triangulo(n):
    for i in range(1, n + 1):
        value = [i] * i
        print(" ".join(map(str, value)))

        # (map(str, value)) = cada value lo va a combertir en un string, siendo recorrido gracias a un map.
        # con el join, lo unimos, separandolo solo por un espacio.

triangulo(5)

for num in range(6):
    for i in range(num):
        print (num, end=" ")
    
    print("\n")