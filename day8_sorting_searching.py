# %%
def merge_sort(list):

    if len(list) == 0:
        return None
    
    if len(list) <=1:
        return list
    
    left, right = split(list)
    left_l = merge_sort(left)
    right_l = merge_sort(right)

    return merge(left_l, right_l)

def split(list):

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    l = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])    
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])    
        j += 1

    return l    
# %%
array = [1000,100,10,8,10,2,10]
# %%
print(merge_sort(array))
# %%
def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_minor_value(values)
        sorted_list.append(values.pop(index_to_move))

    return sorted_list

def index_minor_value(values):
    index_minor = 0
    for index in range(1, len(values)):
        if values[index] < values[index_minor]:
            index_minor = index

    return index_minor        

# %%
print(index_minor_value(array))
# %%
print(selection_sort(array))
# %%
