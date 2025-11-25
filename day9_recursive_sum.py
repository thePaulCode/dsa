# %%
def sum(list):
    """
    Takes O(n) time
    """
    total = 0
    for i in range(0, len(list)):
        total += list[i]
        
    return total

# %%
print(sum([1,2,7]))

# %%

def recursive_sum(list):

    if not list:
        return 0
    print("Calling sum(%s)" % list[1:])
    remaining_value = recursive_sum(list[1:])
    print("Call to sum(%s) returning %d + %d" % (list, list[0], remaining_value))
    return list[0] + remaining_value

# %%
print(recursive_sum([1,2,7,11]))
# %%
