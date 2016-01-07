import random

list = ["Spears", "Avyu", "auru","Nico", "Cris","manu"]
AB =len(list)/2
A=[]

if (len(list)% 2 == 0 ):
    for i in list:
      if AB != i:
          A1 = random.choice(list)
          A.append(A1)
          list.remove(A1)
          print(list)
          print(A)
      else:
          print ("Its not possible with this count", +len(list))
