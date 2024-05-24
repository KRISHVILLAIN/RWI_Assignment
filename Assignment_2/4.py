# define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function.
# invoke myfun2()
def myfun1():
    print("This is myfun1()")

def myfun2():
    print("Invoking myfun1() from myfun2():")
    myfun1()


myfun2()
