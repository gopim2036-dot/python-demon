"""Examples of Python bitwise operators.

Bitwise operators manipulate the individual bits of integer values.
For example, 5 is 0101 and 3 is 0011 in four-bit binary.
"""

a = 5
b = 3
print(f"a = {a} ({a:04b}), b = {b} ({b:04b})")

# AND (&): 1 only where both bits are 1.
print(f"a & b = {a & b} ({a & b:04b})")  # 0001 = 1

# OR (|): 1 where either bit is 1.
print(f"a | b = {a | b} ({a | b:04b})")  # 0111 = 7

# XOR (^): 1 where the bits differ.
print(f"a ^ b = {a ^ b} ({a ^ b:04b})")  # 0110 = 6

# NOT (~): Python defines ~n as -n - 1, so ~5 is -6.
print(f"~a = {~a}")

# Left shift (<<) moves bits left; for non-negative integers, this
# multiplies by 2 for each place shifted.
print(f"a << 1 = {a << 1} ({a << 1:04b})")  # 1010 = 10

# Right shift (>>) moves bits right; for non-negative integers, this
# floor-divides by 2 for each place shifted.
print(f"a >> 1 = {a >> 1} ({a >> 1:04b})")  # 0010 = 2

# Example: use a mask to test whether a particular bit is set.
mask = 0b0010
print("Second bit is set:", bool(a & mask))
