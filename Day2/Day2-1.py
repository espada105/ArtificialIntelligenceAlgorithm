mylist = [30, 10, 20]
print('현재리스트: %s' %mylist)

mylist.append(40)
print('append(40) 후의 리스트: %s' %mylist)

print('pop으로 추출한 값: %s' %mylist.pop())
print('pop 후의 리스트: %s' %mylist)

mylist .sort()
print('sort()후의 리스트: %s' %mylist)

print("revese()")
print('reverse 후의 리스트: %s' %mylist)

print('20값의 위치: %d ' %mylist.index(20))

mylist.insert(2,222)
print('insert(2, 222) 후의 리스트: %s' %mylist)

mylist.remove(2,222)
print('remove(2, 222) 후의 리스트: %s' %mylist)

mylist.extend(77,88,77)
print('extend(77,88,77) 후의 리스트: %s' %mylist)



