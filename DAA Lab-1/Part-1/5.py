def palindrome(string3):
    if len(string3) <= 1:
        return True
    if string3[0] != string3[-1]:
        return False
    return palindrome(string3[1:-1])

input_str = input("Enter a string: ")
print("Input string :",input_str)
if palindrome(input_str):
    print(f" Input is a palindrome.")
else:
    print(f" Input  is not a palindrome.")
