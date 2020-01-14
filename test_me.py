matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]


a = zip(*matrix)
print(list(a))

for i in a:
    # print(list(i))
    print(i)


