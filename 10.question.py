# Given two list of numbers, create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

list1 = [10, 20, 23, 11, 17, 44, 55]
list2 = [13, 43, 24, 36, 12, 33, 66]

def create_list_odd(lists):

    revered_list = []
    for number in lists:
        if  number % 2 == 0 :
            revered_list.append(number)

    return revered_list
    
def create_list_pars(lists):
    pars_numbers = []

    for number in lists:
        if  number % 2 != 0 :
            pars_numbers.append(number)

    return pars_numbers

print( create_list_odd(list1))
print( create_list_pars(list2))