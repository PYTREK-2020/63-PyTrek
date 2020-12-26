ans='y'
while(ans=='y'):
    x=float(input("\nEnter the decimal number: "))
    i=int(x)
    j=x-i
    s=0
    m=1
    a=0
    while(i>0):
        a=i%2
        i=i//2
        if(a==0):
            s=s
        else:
            s=s+(a*m)
        m=m*10

    m=10
    n=0.0
    while(j!=0.0):
        j=j*2
        if(j<1):
            a=0
            n=n
        else:
            a=1
            j=j-1
            n=n+a/m
        m=m*10

    q=s+n
    print("Binary : ",q)

    ans=str(input("Do you want to continue?(y/n) "))
