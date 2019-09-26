def seqsearch(nbrs, tgt):
  for i in range(0, len(nbrs)):
    if (tgt == nbrs[i]):
      return i
  return -1

print(seqsearch([1,2,3], 1))
print(seqsearch([1,2,3], 4))
