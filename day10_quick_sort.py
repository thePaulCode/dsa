# %%
def quicksort(values):
    if len(values) <=1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print("%15s [%1s] %-15s" % (less_than_pivot, pivot, greater_than_pivot))        
    return quicksort(less_than_pivot)+[pivot]+quicksort(greater_than_pivot)

    
# %%
nums = [4,3,2,10,8]
sorted_numbers = quicksort(nums)
print(sorted_numbers)
# %%
def verify(nums):
    if nums[-1] == 80:
        return True
    else: 
        return False
# %%
print(verify(nums))
# %%
