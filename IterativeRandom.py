import itertools ,random

car = list(itertools.product(range(1,14),['Audi','Benz','Bmw','Nissan','Cheverlot','figo','polo','civic']))

random.shuffle(car)

print("You got :")
for i in range(5):
    print(car[i][0], "of" , car[i][1])