
# map
#
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return  n*fact(n-1);
#
#
# print(fact(5));
#
# l=map(fact,[1,2,3,4])
#
# print(list(l))
#
# def add(a,b):
#     return a+b
#
# a=map(add,("ritesh","umesh"),("jadhav","jadhav"))
#
# print(list(a))

# filter
#
# def even(n):
#     return n%2==0
#
# y=filter(even,[12,23,44,23,45,66,47,84])
#
# print(list(y))


# reduce

from functools import reduce

x=reduce(lambda x,y:x+y,range(1,6))

print(x)