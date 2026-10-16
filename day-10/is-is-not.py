a = 10
b = a
print(a is b)  # True, because b references the same object as a
x= 25
y =25
print(x is y)  # True, because small integers are cached in Python
#literals are created once and reused, so x and y reference the same object. 25 will not be created twice in memory.
a=5
print(a is 5)  # False, because a is equal to 5