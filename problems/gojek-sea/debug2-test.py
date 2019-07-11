def binary_search(array, value, low, high):
    if high < low:
        return -1
    else:
        mid = int((low + high)/2); #py2
        if array[mid] > value:
            return binary_search(array, value, low, mid-1) #change
        elif array[mid] < value:
            return binary_search(array, value, mid+1, high)
        else:
            return mid

array = []

for i in range(10000): #py2
    array.append(int(input()))

for i in range(10000): #py2
    value = int(input())
    answer = binary_search(array, value, 0, 9999)
    print("{}".format(answer))