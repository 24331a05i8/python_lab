def modify_list(lst):
    lst.append(100)
    print("Inside function:", lst)

numbers = [1, 2, 3]
modify_list(numbers)
print("Outside function:", numbers)
