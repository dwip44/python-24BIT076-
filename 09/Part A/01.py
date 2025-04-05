def count_lower_upper(string):
    lower = 0
    upper = 0
    for char in string:
        if char.isalpha():
            if char.islower():
                lower += 1
            else:
                upper += 1
    return {'upper': upper, 'lower': lower}

string = "Hello World! 123"
result = count_lower_upper(string)
print(result)
