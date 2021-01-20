def func(**args):
    return args

print(func(arg1=1, arg2=2, arg3=3))

def myfunc(*args):
    print(args)
    return sum(args) * 0.05

print(myfunc(21,53,64,73,23))

def fruits(*args, **kwargs):
    print(args, kwargs)
    if 'fruit' in kwargs:
        print('found {} fruit {}'.format(args[2],kwargs['fruit']))
    else:
        print('no fruit here')

print(fruits(1,2,3,4,5,fruit='kiwi',meat='chito'))





