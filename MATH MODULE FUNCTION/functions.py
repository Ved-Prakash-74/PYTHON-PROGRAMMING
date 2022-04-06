#there are 11 functions in math module

import math
#i) ceil()---->returns integer value greater than the number
print(math.ceil(4.9))
print(math.ceil(4.1))

#ii) floor()---->retuns integer value lesser than than the number
print("\n")
print(math.floor(4.9))
print(math.floor(4.1))

#iii) trunc()----->removes decimal point and prints number before decimal point
print("\n")
print(math.trunc(4.1))
print(math.trunc(123.585))

#iv) fmod()---->performs modulus
print("\n")
print(math.fmod(10,3))

#v) factorial()---->performs factorial of any number
print("\n")
print(math.factorial(5))

#vi) sqrt()----->performs square root
print("\n")
print(math.sqrt(25))

#vii) pow()----->performs exponent
print("\n")
print(math.pow(2,3))

#viii)fabs()----->always returns positive number
print("\n")
print(math.fabs(10.2))
print(math.fabs(-10.2))

#ix) fsum()----->performs sum operation in sequence like list,tuple,set,dictionary
print("\n")
l=[1,2,3,4]
print(math.fsum(l))

#x)gcd()---->prints the greatest common divisor
print("\n")
print(math.gcd(18,24))

#xi)lcm()---->prints the lowest common multiple
print("\n")
print(math.lcm(18,24))

# *****math module constant
print("\n")
print(math.pi)
print(math.e)