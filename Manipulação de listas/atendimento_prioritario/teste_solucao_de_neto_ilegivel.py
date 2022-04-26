def tomarNoCu2(alist):
  for i in range(1,len(alist)):
    flag = True
    cont = i
    while (flag):
      if ((alist[cont]%10) < 6 and (alist[cont-1]%10) >= 6):
        alist[cont-1],alist[cont] = alist[cont],alist[cont-1]
        cont -= 1
      else: flag = False

alist = [54,26,93,17,77,31,44,55,20]
correct = [54,93,31,44,55,20,26,17,77]
tomarNoCu2(alist)
print(alist)
assert alist == correct

