def facto(n):
    f=1 
    for i in range(1,n+1):
        f=f*i
    return f
d={}
while 1:
    n=int(input("Enter any no."))
    f=facto(n)
    print(f)
    d[n]=f
    print('Do you want to continue Y/N')
    if input() !='Y':
        print(d)

    
