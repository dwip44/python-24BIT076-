def ispangram(string):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(string.lower())


string = "The quick brown fox jumps over the lazy dog"
print(ispangram(string))
