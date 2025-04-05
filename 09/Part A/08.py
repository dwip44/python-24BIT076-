def convert(string):
    return ' '.join(sorted(set(string.split())))


string = "Quick brown fox jumps over the lazy dog"
print(convert(string))
