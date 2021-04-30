def f():
    l = []
    for i in range(10):
        l.append(lambda x: i)
    print(l[0](None)) # prints 9
f()