data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]
minval = 99999999

for val in numbers:
  if (minval > val):
      minval = val

print("Minimum value: ", minval)
