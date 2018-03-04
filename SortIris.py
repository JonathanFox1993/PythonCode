with open("data/iris.csv") as f:
   for line in f:
       x = '\n'
       print('{}'.format(line.split(',').remove(x), end = ' '))
