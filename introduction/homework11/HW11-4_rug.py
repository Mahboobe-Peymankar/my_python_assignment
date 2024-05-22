def rug (n):
    
    pattern = ["🌺", "🌿", "🌸", "🌲", "🌻", "🍀", "🌼", "🌿", "🌷",  "🍀", "🍁", "🌳"]
    rug = []
    middle = n//2

    for i in range (n) :
        row = []
        for j in range (n) :
            dis = max (abs ( i - middle) , abs ( j -middle))
            row.append (pattern [dis])
        rug.append (row)
    
    return rug


print ("welcome to my app to create a rug")

while True :
    print ("0 : exit")
    print ("1: continue")
    
    choice = int (input ("please select your choice : "))
    if choice == 0 :
        break
    elif choice == 1 :
        n = int (input ("please enter an odd number to generate a rug : "))

        if n % 2 == 0 :
            print ("Invalid input.") 
        
        elif n % 2 != 0 :

            print ("\n\n")
            result = rug (n)
            for row in range (n) :
                for col in range (n) :
                    print (result [row] [col], end = "  ")
                print ("\n")
            
    else :
        print ("please select a correct choice between 0 and 1")
