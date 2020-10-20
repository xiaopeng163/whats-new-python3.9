d1 = {'id': 5, 'username': 'user1', 'email': 'user1@gmail.com'}
d2 = {'email': 'user1@python.org'}

# expected result
# {'id': 5, 'username': 'user1', 'email': 'user1@python.org'}

# update d1
# d1.update(d2)
# print(d1)

# print({**d1, **d2})
# d3 = {**d1, **d2}
# print({**d2, **d1})

# new in python3.9
print(d1 | d2)
d3 = d1 | d2
print(d1)

a = 1
b = 2
a += b


d1 |= d2
print(d1)
