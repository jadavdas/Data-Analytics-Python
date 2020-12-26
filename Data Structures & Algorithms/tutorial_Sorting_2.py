#%% Bubble Sorting: Implementaion 1

def bubblesort(alist):
    # swap the elements
    n = len(alist)
    for item_num in range(n-1, 0, -1):
        for idx in range(item_num):
            if alist[idx] > alist[idx+1]:
                temp = alist[idx]
                alist[idx] = alist[idx+1]
                alist[idx+1] = temp   
    return alist      
unsorted_list = [19,2,31,45,6,11,121,27]
sorted_list = bubblesort(unsorted_list)
print(sorted_list)

#%% Bubble Sorting: Implementation 2

def bubblesort(alist):
    # swap the elements
    n = len(alist)
    for i in range(0, n-1):
        for j in range(i+1, n-1):
            if alist[i] > alist[j]:
                temp = alist[i]
                alist[j] = alist[i]
                alist[i] = temp   
    return alist      
unsorted_list = [19,2,31,45,6,11,121,27]
sorted_list = bubblesort(unsorted_list)
print(sorted_list)

#%% Merge sort
from numpy import*

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [19,2,31,45,6,11,121,27]

print(merge_sort(unsorted_list))

        
        