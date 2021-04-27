is_even = lambda num: (num & 1) == 0
is_odd = lambda num: (num & 1) == 1

print("is_even(0)", is_even(0))
print("is_even(-1)", is_even(-1))
print("is_odd(0)", is_odd(0))
print("is_odd(1)", is_odd(1))
