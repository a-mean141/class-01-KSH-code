data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]

def RecursiveArraySum(nbrs, k):
  if k == 0:
    return nbrs[0]
  return RecursiveArraySum(nbrs, k - 1) + nbrs[k]

print("Recursive Array Sum:", RecursiveArraySum(numbers, len(numbers) - 1))
