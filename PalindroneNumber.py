num = input("Enter a number: ")

if num == num[::-1]:
    print(num, "is a Palindrome number")
else:
    print(num, "is NOT a Palindrome number")
