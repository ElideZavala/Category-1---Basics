# Write code to extract each digit from the integer, in the reverse order


#? Forma 1

# integer = 33154689

# def reverse_integer(num):
#     num_str = str(num)

#     num_list = list(num_str)
#     reverse_numers = num_list[::-1]

#     return int(''.join(reverse_numers))

# interger_reverse = reverse_integer(integer)
# print(interger_reverse)


#? Forma 2
integer = 33154689

while (integer > 0):
    digit = integer % 10 # Obtenemos el ultimo digito del numero
    integer = integer // 10   # Elimina el último dígito del número
    
    print(digit, end="" ) # Permite que todos los digitos se formen en una sola linea. 
