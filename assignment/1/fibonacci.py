import time

def iterfibo(n):
  x, y = 1, 1
  for i in range(2, n):
    x, y = y, x + y

  return y

def fibo(n):
  if n <= 2:
    return 1
  return fibo(n - 1) + fibo(n - 2)

while True:
  nbr = int(input("Enter a number: "))
  if nbr <= 0:
    break
  ts = time.time()
  fibonumber = iterfibo(nbr)
  ts = time.time() - ts
  print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
  ts = time.time()
  fibonumber = fibo(nbr)
  ts = time.time() - ts
  print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
