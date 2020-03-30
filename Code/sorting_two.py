#iterate through array
#check if value is greater than or less than next value
#if value is not greater, return false
#out of loop, return true

def check_sort(sort_array):
    for i in range(0, len(array)):
        if (array[i] > array[i+1]) and (array[i] != array[len(array)]):
            return False
        return True

#iterate through array, while sorted variable is false
#check each value and swap if greater than the next, set temp boolean to false
#set sorted to equal true once temp_boolean equals true

def bubble_sort(sort_array):
    sorted = False
    while sorted is not True:
        sorted_temp = True
        for i in range(0, len(sort_array)-1):
            if sort_array[i] != sort_array[len(sort_array)-1]:
                if sort_array[i] > sort_array[i+1]:
                    sorted_temp = False
                    temp_value = sort_array[i]
                    sort_array[i] = sort_array[i+1]
                    sort_array[i+1] = temp_value
        if sorted_temp is True:
            sorted = True
    return sort_array

print(bubble_sort([0,1,4,3,2]))
