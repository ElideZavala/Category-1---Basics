# Print the result of the multiplication of two sets of integers if it is less than 1000. If the result is greater that 1000, print their sum.

def operation(valor1, valor2):
    multiiple = valor1 * valor2 

    if multiiple <= 1000:
        return multiiple
    else :
        return valor1 + valor2

num1 = 25
num2 = 26

caso1 = operation(num1, num2)
print("caso1,",caso1)


num1 = 35
num2 = 36

caso2 = operation(num1, num2)
print("caso2:", caso2)

