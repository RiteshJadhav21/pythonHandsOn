

def fun1(fun2):
    def fun3():
        print("before working")
        fun2()
        print("after working")
    return fun3

# @fun1
def work():
    print("I'm working")

# work = fun1(work);

work()

