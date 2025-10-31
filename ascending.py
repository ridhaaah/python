my_dict = {'a':3, 'c':1, 'b':2}
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Original dictionary:", my_dict)
print("Ascending order:", ascending)
print("Descending order:", descending)
