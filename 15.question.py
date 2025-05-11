# Write a function called exponent(base, exp) that returns an int value of base raised to the power of exp.
# def exponent(base, exp):
#     return base ** exp

# print(exponent(5 , 4))

def exponent(base, exp):
    num = exp
    result = 1

    while num > 0:
        result = result * base
        print(result) # 5, 25, 125, 625, None
        num = num - 1

print(exponent(5 , 4)) # 625