#bubble sorting algorithm to sort a list of numbers
def bubble_sort(arr):
    #get the total number of length of the array to iterate
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

print(bubble_sort([1,53,33,234,2636235,-5]))