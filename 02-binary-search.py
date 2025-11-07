# %%
def binary_search(list, target):
    first = 0
    last = len(list)-1

    while (first <= last):
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint - 1
    return None        

# %%
def verify(index):
    if index is not None:
        print("O target está presente na posição: ", index )
    else:
        print("O target NÃO está presente na lista. ")

# %%
target = 2

array = [2, 4, 6, 8, 10, 12]

resultado = binary_search(array, target)

verify(resultado)
# %%

# %%
