def frequency(string):
    words = string.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return sorted(freq.items())

string = "Quick brown fox jumps over the lazy dog"
print(frequency(string))
