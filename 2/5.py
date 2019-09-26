scoredb = [
  {
    'Name': 'Lee',
    'Score': 30
  },
  {
    'Name': 'Kim',
    'Score': 40
  },
  {
    'Name': 'Park',
    'Score': 50
  },
  {
    'Name': 'Choi',
    'Score': 90
  }
]
def findScoreDB(scdb, keyname):
  for i in range(0, len(scdb)):
    if (keyname == scdb[i]['Name']):
      return i
  return -1

name = input("Enter name: ")
idx = findScoreDB(scoredb, name)
if (idx > -1):
  print(scoredb[idx])
else:
  print("No such Name")
