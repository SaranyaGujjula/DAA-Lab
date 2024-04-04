def reverse_str(string2):
    if len(string2) <= 1:
        return string2
    else:
        return reverse_str(string2[1:]) + string2[0]

input_str = "pots&pans"
rev_str = reverse_str(input_str)
print("Reversed string:", rev_str)
