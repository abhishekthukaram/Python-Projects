def balancedlist(input_list):
    break_list = []
    for i in range(len(input_list)):
        if sum(break_list) != sum(input_list):
            temp = input_list.pop(0)
            break_list.append(temp)
        else:
            break
    return break_list, input_list


print(balancedlist([1,2,3,4,5,6,7,2]))