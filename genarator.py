def evenNumbers(n):
    i=1
    while n:
        yield 2*i
        i+=1
        n-=1

itr = evenNumbers(10)
even_list=[]

while True:
    try:
        even_list.append(next(itr))
    except StopIteration:
        break



print(even_list)
