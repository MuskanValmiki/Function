def prime():
    i=2
    c=1
    num1=int(input("enter a prime number"))
    while i<=num1:
        if num1%i==0:
            c+=1
        i+=1
    if c==2:
        return (num1,"prime")
    else:
        return (num1,"not prime")
def armstrong():
    num2=input("enter a number")
    b=len(num2)
    m=int(num2)
    n=m
    sum=0
    while m>0:
        c=m%10
        sum=sum+c**b
        m=m//10
    if n==sum:
        return (n,"armstrong")
    else:
        return (n,"not armstrong")
def harsadh():
    num3=int(input("enter a number"))
    m=num3
    sum=0
    while num3>0:
        c=num3%10
        sum=sum+c
        num3=num3//10
    if m%sum==0:
        return (m,"harsadh")
    else:
        return (m,"harsadh")
def perfect():
    num4=int(input("enter a number"))
    m=num4
    i=1
    sum=0
    while i<num4:
        if num4%i==0:
            sum=sum+i
        i+=1
    if m==sum:
        return (m,"perfect")
    else:
        return (m,"not perfect")
def main():
    print(prime())
    print(armstrong())
    print(harsadh())
    print(perfect())
main()
# here we are checking all number