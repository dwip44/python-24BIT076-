dictionary1 = {"key1": "value1", "key2": "value2"}
dictionary2 = {"key3": "value3", "key4": "value4"}
dictionary3 = {"key5": "value5", "key6": "value6"}

dictionary4 = {**dictionary1, **dictionary2, **dictionary3}

print("Concatenated Dictionary:")
print(dictionary4)
