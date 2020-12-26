#%% 1 : finding a number in an array

def BinarySearch(A,n,x):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if x == A[mid]:
            return mid
        elif x < A[mid]:
            high = mid-1
        else:
            low = mid+1
        
#A = [2, 4, 10, 10, 10, 18, 20]
#A = [2, 10]
A = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
x = 5
n = len(A)
index = BinarySearch(A,n,x)
print("Index:", index)

#%% 2 : finding lowest index a number in an array

def BinarySearch(A,n,x):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if x == A[mid]:
            result = mid
            high = mid-1 
        elif x < A[mid]:
            high = mid-1
        else:
            low = mid+1
    return result
        
A = [2, 4, 10, 10, 10, 18, 20]
#A = [2, 10]
x = 10
n = len(A)
index = BinarySearch(A,n,x)
print("Index:", index)

#%% 3 : finding highest index a number in an array

def BinarySearch(A,n,x):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if x == A[mid]:
            result = mid
            low = mid+1 
        elif x < A[mid]:
            high = mid-1
        else:
            low = mid+1
    return result
        
A = [2, 4, 10, 10, 10, 18, 20]
#A = [2, 10]
x = 10
n = len(A)
index = BinarySearch(A,n,x)
print("Index:", index)

#%% 4 : find count of an element in an array: BigO(n) - all scenarios

def CountNumber(A,n,x):
    count = 0
    for i in range(0,n):
        if A[i] == x:
            count += 1
    return count
A = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
n = len(A)
x = 5
count = CountNumber(A,n,x)
print("Count:",count)

#%% 5 : find count of an element in an array: BigO(n) - worst scenarios

def CountCountNumber(A,n,x):
    count = 0
    for i in range(0,n):
        if A[i] == x:
            count += 1
        elif A[i] > x: 
            break  # because the array is sorted
    return count
A = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
n = len(A)
x = 5
count = CountCountNumber(A,n,x)
print("Count:",count)

#%% 6 : find count of an element in an array: BigO(n) - worst scenarios

def CountCountNumber(A,n,x):
    count = 0
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if A[mid] == x:
            result = mid
            count += 1
        elif x < A[mid]:
            high = mid-1
        else:
            low = mid+1
            
    for i in range(result+1,n):
        if A[i] == x:
            count += 1
        elif x > A[i]:
            break
            
    for i in range(result-1,0,-1):
        if A[i] == x:
            count += 1
        elif A[i] < x: 
            break  # because the array is sorted
    return count

A = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
n = len(A)
x = 4
count = CountNumber(A,n,x)
print("Count:",count)


#%% 7: find count of an element in an array: BigO(log(n)) - worst scenarios

def CountNumber(A,n,x,searchFirst):
    low = 0
    high =  n-1
    result = -1
    while low <= high:
        mid = (low+high)//2
        if x == A[mid]:
            result = mid
            if searchFirst==True:
                high = mid-1
            else:
                low = mid+1
        elif x < A[mid]:
            high = mid-1
        else:
            low = mid+1
    return result
    
A = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
n = len(A)
x = 5
firstIndex = CountNumber(A,n,x,True)
if firstIndex == -1:
    print("Count = 0")
else:
    lastIndex = CountNumber(A,n,x,False)
    print("count = ", lastIndex - firstIndex + 1)
    
#print("firstIndex:",firstIndex)
#print("lastIndex:",lastIndex)