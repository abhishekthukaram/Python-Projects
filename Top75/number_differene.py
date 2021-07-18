def check_difference(input_list, diff_element):
    compare = sorted(input_list)
    count_diff = 0
    i , j = 0,1
    while j < len(input_list):
        if compare[j] - compare[i] == diff_element:
            count_diff+=1
        i+=1
        j+=1
    return count_diff


print(check_difference([1, 2, 4, 5, 6, 0], 1))
