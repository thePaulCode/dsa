# %%
def recursive_binary_search(list, target):
    if len(list) == 0: 
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint-1], target)

def verify(result):
    print("Target found:", result)                        

# %%
array = [0,2,4,6,8,10,12]

target = 100

response = recursive_binary_search(array, target)
verify(response)
# %%
def rec_binary(arr, target):
    # stop condition 1
    if len(arr) == 0:
        return False
    
    midpoint = len(arr)//2
    # stop condition 2
    if arr[midpoint] == target:
        return True
    else:
        if arr[midpoint] < target:
            # base case
            return rec_binary(arr[midpoint+1:], target)
        else:
            return rec_binary(arr[:midpoint-1], target)
# %%
saida = rec_binary(array, target)    
verify(saida)    
# %%
