import random
n = int (input ( "please enter a size of aaray between 1 and 100..." ))
array = []
i = 0
while i < n :

    x = random.randint ( 1 , 10 )
    if x in array :
        continue

    else :
       array.append ( x )
       i += 1
print ( array )      
      



