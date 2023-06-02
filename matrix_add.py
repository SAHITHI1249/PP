list1 = [[1,2],[1,2]]
list2 = [[1,2],[1,2]]
list3 = [[0,0],[0,0]]
for i in range(len(list1)):
  for j in range(len(list2)):
    list3[i][j] = list1[i][j] + list2[i][j]
print("list1:")
for i in list1:
  print(i)
print("list2:")
for i in list2:
  print(i)
print("sum :")
for i in list3:
  print(i)

    
