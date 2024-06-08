def sum_of_squares(elements_list):
    for i in range (len(elements_list)):    
        elements_list[i]=elements_list[i]**2
        
    return sum(elements_list)
print("Enter The Numbers supprated by cama (,)")
elements_list=list(map(int,input().split(",")))
print("Sum of Squares_list is : "+str(sum_of_squares(elements_list)))

