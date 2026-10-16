# in python strings are immutable, which means we cannot change the value of a string once it is created.

s1 = "hello world"

s2 = ["k"]
s2[0] = "m"
print(s2)  # Output: karri

# slicing of python can be done using the slice operator [:] which is used to extract a portion of the string.
# s1 is defined as "hello world" and we are slicing it from index 0 to 5 which will give us "hello"


print(s1[0:5])  # Output: hello
print(s1[6:])  # Output: world
print(s1[0:7:2])  # Output: hello s1(start index:stop index:step jump)
#dlrow olleh
print(s1[-3:-9:-1])  # Output: worl