# 10 challenge , a sequence to be find 

# input
a = [1, 11, 21, 1211, 111221]

# len(a[30]) = ?

a0 = 1
a1 = 11
a2 = 21
a3 = 1211
a4 = 111221

# after asking the AI, turnes out it's a famous pattern called : 'look and say sequence'
#  1 // one 1 == 11 // two ones == 21 // one two one one == 1211 // one one one two two ones == 111221
# print (a[30])
#  we nee to construct an algorithm to construct the sequence



input1 = [1]
# we need a function to add the next element
def look_and_say(last_element):
    # the input is a number
    last_element_str = str(last_element)
    print ('this is the input = ',last_element)
    
    # print ('length = ',length)
    list_numbers_split = []
    # this loop is for split and assemble together
    for char in last_element_str :
        if list_numbers_split == []:
            list_numbers_split.append(char)
        else:
            if list_numbers_split[-1][-1] == char:
                list_numbers_split[-1] += char
            else:
                list_numbers_split.append(char)
    print ('this is the list after splitting and assembling = ',list_numbers_split)   
    # we need another loop to draw the new number
    new_number = ''
    for num in list_numbers_split:
        len_portion = len(num)
        portion = num[0]
        new_number = new_number + str(len_portion) + portion
    print ('this is the new number = ', new_number)
    return new_number

# we will generate as much as we need of look-and-say sequence
def find_nth_order(order):
    # we start with a list of one element 
    list = [1]
    length = 1
    while length< order:
        last_element = list[-1]
        list.append(look_and_say(last_element))
        length = len(list)
    print  (f'final list with order = {length} is ={list} ')
    return list
    
# look_and_say(111221)
a = find_nth_order(31)
# look_and_say(111221)
print (f'the length of a[30] = {len(a[30])}') 

# nice ! nailed it , the len(a[30]) = 5808  