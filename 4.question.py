#  Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def remove_chars(str, num):
    return str[num:] # Con el num: obtenemos el resto de los valores


print(remove_chars("learning", 4)) # Output: ning
