def perfect(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum+=i
        i+=1
    if sum==num:
        return num,"perfect number"
num=int(input("enter any number="))
function=perfect(num)
# print(perfect(num))

# here we check it is perfect number or not part1




