#
## list maker
### Created by Yseeva
##
#

import random

print("<----- WELCOME ----->")
n=int(input("How many object you want your list have ? "))

def fill_list_without_repeats(n):
    original_list = list(range(1, n+10))
    random.shuffle(original_list)
    new_list = original_list[:n]
    return new_list


result = fill_list_without_repeats(n)
print("The list you want to have is :" , result)