def func(str , n):
  if n > 0:
    func("func", n-1)
    print(str, "called func with n =", n)

def main():
  func("main" , 7)

main()