data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]
minval = numbers[0]

for val in numbers:
  if (minval > val):
      minval = val

print("Minimum value: ", minval)
