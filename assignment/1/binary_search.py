import time

def recursive_binray_search(arr, n, lower, upper):
  if upper < lower:
    return -1
  mid = (lower + upper) // 2

  if arr[mid] == target:
    return mid
  elif target < arr[mid]:
    return recursive_binray_search(arr, n, lower, mid - 1)
  else:
    return recursive_binray_search(arr, n, mid + 1, upper)

data = input("Enter list of sorted numbers: ")
target = int(input("Enter target number: "))
arr = [int(i) for i in data.split()]
ts = time.time()
lower = 0
upper = len(arr) - 1
idx = -1

while (lower <= upper):
  middle = int((lower + upper) // 2)
  if arr[middle] == target:
    idx = middle
    break
  elif arr[middle] < target:
    lower = middle + 1
  else:
    upper = middle - 1

ts = time.time() - ts
print("target index %d time %.6f" %(idx, ts))
ts = time.time()
idx = recursive_binray_search(arr, target, 0, len(arr) - 1)
ts = time.time() - ts
print("target index %d time %.6f" %(idx, ts))
