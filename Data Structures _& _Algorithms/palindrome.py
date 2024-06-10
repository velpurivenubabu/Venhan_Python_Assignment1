def is_palindrome(s: str) -> bool:
    s1=s
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return s1 +" is a palindrome"
    else:
        return s1 +" is not a palindrome"

print("Enter The String")
string=input()
print( is_palindrome(string))