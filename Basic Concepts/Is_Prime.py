
def is_prime(n):
    is_prime_number=True
    if n<2:
        is_prime_number=False
    else:
        for i in range(2,n):
            if n%i==0:
                is_prime_number=False
                break
    if (is_prime_number):
        return (str(n)+" is Prime Number")
    else:
        return(str(n)+" is not a Prime Number")


print("Enter the Number")
number=int(input())    
print(is_prime(number))