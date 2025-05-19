print("Enter a string to check palindrome or not")
str=input()

strrev=(str[::-1])

if strrev ==str:
    print("It is Palindrome")
else:
    print("It is not Palindrome")
