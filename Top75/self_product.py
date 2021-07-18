"""
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers
present in the list except the number stored at that index.
"""

def find_product(lst):
    output = []
    prod_until_now = 1
    for i in range(len(lst)):
        current_product = 1
        for j in range(i+1, len(lst)):
            current_product = current_product*lst[j]
        output.append(current_product*prod_until_now)
        prod_until_now = prod_until_now*lst[i]
    return output


print(find_product([1,2,3,4]))
print(find_product([1,2,3,4,5]))