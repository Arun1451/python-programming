dict1 = {"a": 6, "b": 1, "c": 0}
sorted_values = sorted(dict1.values()) 
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)
