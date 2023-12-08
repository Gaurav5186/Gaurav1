def countOccurrances(n, d):
    count = 0
 
    while (n > 0):
 
       
        if(n % 10 == d):
            count = count + 1
  
        n = n // 10
 
    return count

d = 2
n = 828282
print(countOccurrances(n, d))
