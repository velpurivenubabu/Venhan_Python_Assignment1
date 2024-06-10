
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    first_half = merge_sort(arr[:middle])
    second_half = merge_sort(arr[middle:])
    
    return merge(first_half,  second_half)

def merge(first_half, second_half):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len( first_half) and right_index < len(second_half):
        if  first_half[left_index] < second_half[right_index]:
            merged.append( first_half[left_index])
            left_index += 1
        else:
            merged.append(second_half[right_index])
            right_index += 1
    
    merged.extend(first_half[left_index:])
    merged.extend( second_half[right_index:])
    
    return merged
print("Enter list of Numbers supperated by coma(,)")
arr = list(map(int,input().split(",")))
sorted_arr = merge_sort(arr)
print(sorted_arr)
