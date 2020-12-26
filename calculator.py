
def factorial(q):
    j=0
    if(q==1 or q==0):
        return 1
    else:
        j=q*factorial(q-1)
        return j

a='y'
while a == 'y':
    print('''\nTRIGONOMETRY CALCULATOR:
1.sin(x)
2.cos(x)
3.tan(x)
''')

    n=int(input("Enter your choice: "))
    x=float(input("Enter the value of \'x\' in degree: "))
    t=-1
    x=x*(22/7)/180
    
    if(n==1):
        s=x
        m=0
        for m in range(3,153):
            s=s+ t*(x**m)/factorial(m)
            t=-1*t
            m=m+2
        print(s)

    elif(n==2):
        c=1
        m=0
        for m in range(2,152):
            c=c + t*(x**m)/factorial(m)
            t=t*-1
            m=m+2
        print(c)

    else:
        tn=0
        s=x
        c=1
        h=0
        k=0

        for h in range(3,153):
            s=s+ t*(x**h)/factorial(h)
            t=-1*t
            h=h+2

        for k in range(2,152):
            c=c + t*(x**k)/factorial(k)
            t=-1*t
            k=k+2

        tn=s/c
        print(tn)

    a=str(input("\nWanna continue?(y/n)  "))
    if a == "n":
        break
      
    
       
    
