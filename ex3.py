data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]
curruent_sum = 0

for val in numbers:
  curruent_sum += val

print("Sum value: ", curruent_sum)
print("Average value: ", curruent_sum / len(numbers))
