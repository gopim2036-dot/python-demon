s1= "hi how are you"

# below statement will output the type of s1 which is string.
print(type(s1))  # Output: <class 'str'>

# below statement will ouptut the list of all the methods and attributes of string class.
#print(dir(s1))  # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust']

#prints the starting index of the substring "how" in the string s1. If the substring is not found, it will return -1.
print(s1.find("how"))

# return -1 as the substring "key" is not present in the string s1.
print(s1.find("key")) 

#find method returns the index of the first occurrence of the substring "are" in the string s1. If the substring is not found, it will raise a ValueError. 
print(s1.find("o"))

#find method returns the index of the first occurrence of the substring "o" in the string s1, starting from index 5 and ending at index 15. If the substring is not found, it will return -1.
print(s1.find('o',5,15,))

# this method returns the index of the last occurrence of the substring "o" in the string s1, starting from index 0 and ending at index 15. If the substring is not found, it will return -1.
print(s1.rfind('o',0,15))  # Output: -1

#this mentioned method returns the number of occurrences of the substring "o" in the string s1. If the substring is not found, it will return 0.
print(s1.count("o"))  # Output: 2

# index menthod works same as find method but the difference is that if the substring is not found, it will raise a ValueError instead of returning -1.