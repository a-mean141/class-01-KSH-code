def RecursiveSum(n):
  return 1 if n == 1 else RecursiveSum(n - 1) + n
upper = int(input("Enter a number: "))
print("Recursiv Sum of 1 to", upper, "=", RecursiveSum(upper))
