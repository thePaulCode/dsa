# %%
def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the dorted sublists created in previous step

    Takes O (n log n) time
    """
    # Stop condition 
    if len(list) == 0:
        return None
    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """ 
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and rigth

    Tuns in overall O (log n) time
    """   
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right

def merge(left, right):
    """ 
    Merge two lists (arrays), sorting them in the process
    Return a new merged list
    Runs in overall O (n) time
    """    
    l = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            l.append(left[i])
            i +=1
        else:
            l.append(right[j])
            j +=1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[i])
        j += 1    

# %%
def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

# %%
alist = [54,62,93,7,77,21,9]

# %%
print(verify_sorted(alist))

# %%
