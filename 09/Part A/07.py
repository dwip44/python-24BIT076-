def ispalindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


string = "Hello There"
print(ispalindrome(string))
