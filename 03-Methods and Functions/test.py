arr = []
usrIn = 0
#set to false
rand = 0
while False:
    usrIn = int(input('your guess: '))
    arr.append(usrIn)
    print(usrIn, arr)
    if usrIn < 1 or usrIn > 100:
         print('foo, invalid input')
    if usrIn < rand:
         print('more')
    if usrIn > rand:
         print('less')
     if usrIn == rand:
         print('You got it!!')
         break


stocks = [('apple', 666), ('google', 400), ('msft', 111)]
total = 0
for na,pi in stocks:
    print(na)
    print(pi)
    total+=pi
print(total)
