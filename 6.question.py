# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

list = [10, 20, 33, 46, 55, 77, 105, 204, 335]

def divid_of_five(numbers):
    for num in numbers:
        if (num % 5 == 0):
            print(f"{num}, {num} % 5 = {num%5}")


divid_of_five(list)

