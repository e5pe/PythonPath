
my_string = 'abcdarioc'

for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')

print('\n'+('*'*30))
cars = ["bmw", "benz", "seat"]

for car in cars:
    print(car)


numbers = [1, 2, 3]
for n in numbers:
    print(n*10)

d = {'uno': 1, 'dos': 2, 'tres': 3}
for k in d:
    print(k + " "+str(d[k]))

for k, v in d.items():
    print(k+" "+str(v))
