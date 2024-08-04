# None 

# None means nothing
# no values associated
# there are some situations where values are not available
# for that situation, None is there

def f1():
    return 10

x = f1()
print(x)


def f2():
    print("Helllooo")

x = f2()
print("=>",x)


a = None
print(id(a))
print(type(a))


# All refer to same none object (below eg)
a = None
b = None
c = None

# this method is null
def f1():
    pass

d = f1()

print(a,"=>",b,"=>",c,"=>",d)
print(id(a),"=>",id(b),"=>",id(c),"=>",id(d))

