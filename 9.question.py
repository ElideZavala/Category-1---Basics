# # Reverse a given number and return true if it is the same as the original number

num1 = 323
num2 = 625

# # - conver a string
# # - ordenarl al reverso
# # - convertir a number
# # si es igual o aldividir es igual a 0 retornar true

# def retornEqual(num):
    
#     numList = [int(num) for num in str(num)] # Creamos el numero en un string y luego lo agregamos como un numero en una lista. 
#     reversaList = numList[::-1] # regresamos la lista al revez

#     revesaNum = int(''.join(map(str, reversaList))) # Convertimos cada numero en string y luego lo juntamos, quitandoles los espacios    
#     if ( num % revesaNum == 0): # si la divicion entre cada uno da 0, el resultado sera True de los contrario sera False. 
#         return True
#     else:
#         return False 


# print(retornEqual(num1)) # True
# print(retornEqual(num2)) # False


def reverse_check(number):
    print("Numero original", number)

    original_number = number
    reversed_num = 0

    while (number > 0):
        remaider = number % 10

        reversed_num = (reversed_num * 10) + remaider # Reordenamos el numero al revez
        
        number = number // 10 

    if original_number == reversed_num:
        return True
    else:
        return False

print(reverse_check(num1))
print(reverse_check(num2))

