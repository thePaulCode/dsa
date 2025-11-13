# %%
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("O target está presente na posição: ", index )
    else:
        print("O target NÃO está presente na lista. ")

# %%
target = 10

array = [2, 4, 6, 8, 10, 12]

resultado = linear_search(array, target)

verify(resultado)

# %%
