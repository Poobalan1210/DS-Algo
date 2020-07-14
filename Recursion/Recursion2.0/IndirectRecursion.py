def func1(string,n):
    if n>0:
        print(string,"called func1 on n =",n)
        func2("func1",n-1)

def func2(string,n):
    if n>0:
        print(string,"called func2 in n =",n)
        func1("func2",n-1)

def main():
    func1("main",7)

main()