
#open the file iris without having to say close
with open("data/iris.csv") as f:
   #loop through each line
   for line in f:
       #print out each line and format them correctly 
       print('{}'.format(line.split(','), end = ' '))
