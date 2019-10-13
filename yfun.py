
#MyFunction Library

#Get binary of number
#this method accepts an integer and returns a string
def getBinary(g):
    b=""
    
    while g != 0:
        b = b + str(g&1)
        g >>= 1

    b = b[::-1]
    return b


#Count 1's and 0's in a binary of a number
#this method accepts string format number and an integer what
#what is 1 means count number of 1's in the binary
#what is 0 means count number of 0's in the binary
def countInBinary(s, what):
    count=0
    for i in s:
        if int(i)==what:
           count += 1 
    return count


