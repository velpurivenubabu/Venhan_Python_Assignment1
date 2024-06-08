

def find_duplicates(arr):
    my_list= []
    duplicates_list = []

    for element in arr:
        if element in  my_list:
            duplicates_list.append(element)
        else:
             my_list.append(element)

    return duplicates_list
print("Enter list of Numbers supperated by coma(,)")
arr = list(map(int,input().split(",")))
print("Duplicates in the list:", find_duplicates(arr))
