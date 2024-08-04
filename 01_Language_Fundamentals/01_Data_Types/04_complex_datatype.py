# Complex data type (symbol should be j only, no other symbol)
# a + bj, where
#               => a = real part
#               => b = imaginary part
#               => j^2 = -1
#               => j = under-root(-1)
x = 10+20j
print(type(x))
print(x.real)
print(x.imag)

# these all are acceptable
a = 10+20j
b = 10.5+20j
c = 10.5+20.6j
d = 0b1111+20j
# e = 15+0b1111j  => syntax error



x = 10+20j
y = 20+30j

print(x+y)
print(x*y)
print(x/y)