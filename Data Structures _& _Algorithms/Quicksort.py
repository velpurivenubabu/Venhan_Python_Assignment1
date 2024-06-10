def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

print("Enter numbers supprate with coma(,)")
arr=list(map(int,input().split(",")))
print(quicksort(arr))