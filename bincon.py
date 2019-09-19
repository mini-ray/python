# bincon.py
# Convert a base 10 number to binary
# Use n191 base 10 equal to 1011 1111 base 2
# q(quotient) d(divisor) r(remainder) n(integer input)
# div 128
n = int(input("Input an integer less than 256 : "))
d = 128
q = int(n / d)
r = int(n % d)
print(d, q,r)
n = r
b128 = q
# div 64*****
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d, q,r)
n = r
b64 = q
# div 32*****
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d, q,r)
n = r
b32 = q
# div 16*****
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d, q,r)
n = r
b16 = q
# div 8*****
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d, q,r)
n = r
b8 = q
# div 4*****
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d, q,r)
n = r
b4 = q
# div 2*****
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d, q,r)
n = r
b2 = q
# div 1*****
d = int(d / 2)
q = int(n / d)
r = int(n % d)
print(d, q,r)
n = r
b1 = q

print(str(b128) + str(b64) + str(b32) + str(b16) + " " + str(b8) + str(b4) + str(b2) + str(b1))
