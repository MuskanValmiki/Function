def prime():
    i=2
    c=1
    num1=int(input("enter a prime number"))
    while i<=num1:
        if num1%i==0:
            c+=1
        i+=1
    if c==2:
        return (num1)
    else:
        return (num1)
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
        return (n)
    else:
        return (n)
def harsadh():
    num3=int(input("enter a number"))
    m=num3
    sum=0
    while num3>0:
        c=num3%10
        sum=sum+c
        num3=num3//10
    if m%sum==0:
        return (m)
    else:
        return (m)
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
        return (m)
    else:
        return (m)
def main():
    empty=[]
    empty.append(prime())
    empty.append(armstrong())
    empty.append(harsadh())
    empty.append(perfect())
    index=0
    max=0
    while index<len(empty):
        if empty[index]>max:
            max=empty[index]
        index+=1
    return max
print(main())
# which number is greater that number you will print
