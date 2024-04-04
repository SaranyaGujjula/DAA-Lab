def str_to_int(string1): 
    string = string1.replace(',', '')
    if not string:
        return 0
    digit = int(string[-1])
    integer_value = str_to_int(string[:-1])
    return integer_value * 10 + digit


input_str = input("Enter a string of digits: ")
result = str_to_int(input_str)
print("input string ",input_str)
print("Integer representation:", result)
