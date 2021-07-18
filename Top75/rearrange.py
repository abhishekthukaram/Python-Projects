"""
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear
on the left and positive elements appear at the right of the list.
Note that it is not necessary to maintain the sorted order of the input list.
"""

def rearrange(lst):
    left = 0
    right = len(lst)-1
    while left <= right:
        if lst[right] <0 and lst[left] >=0:
            lst[left], lst[right] = lst[right], lst[left]
            left+=1
            right-=1
        elif lst[right]>0:
            right-=1
        elif lst[left] <0:
            left+=1
    return lst


"""
Method2
"""
def rearrange_option2(lst):
    result = []*len(lst)
    for i in lst:
        if i < 0:
            result.insert(0,i)
            print("Negat", result)
        elif i >=0:
            result.insert(len(lst)-1,i)
            print("Posit",result)
    lst= result
    return lst


print(rearrange([10,-1,20,4,5,-9,-6]))
print(rearrange_option2([10,-1,20,4,5,-9,-6]))