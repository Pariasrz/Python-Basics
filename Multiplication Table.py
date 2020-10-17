
#x = int(input("Enter the rows \n"))
#y = int(input("Enter the columns \n"))
def multiplication_table(x, y):
    for i in range(1, y+1):
        for j in range(1, x+1):
            print (i * j , "\t")
multiplication_table(9, 9)