# Calculate income tax for the given income by following the below rules

"""
Taxable Income	                      Rate (in %)
First  $10,000	                      0
Next   $10,000	                      10
The remaining                       	20

"""

# Metodo 1
# def calculate_tax(income):
#     if income <= 10000:
#         return 0
#     elif income <= 20000:
#         return (income - 10000) * 0.10
#     else:
#         return (10000 * 0.10) + ((income - 20000) * 0.20)

# tax = calculate_tax(45000)
# print(tax) 


# Metodo 2
income = 45000
tax_payable = 0

print("Given income:", income)

if (income <= 10000): # si es menor o igual a 10000 no aplicamos inpuestos
    tax_payable = 0
elif income <= 20000: # si es menor o igual a 20000, aplicamos un 10%
    tax_payable = (income - 10000) * 10 / 100
else:
    tax_payable = 0 # si es mayor lo regresamos a cero
    tax_payable = 10000 * 10 / 100 # aplicamos el descuento del 10%

    tax_payable += (income - 20000) * 20 / 100 # mas otro 20% al restante 

print(tax_payable)
