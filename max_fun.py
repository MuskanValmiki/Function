def odd():
    i=0
    while i<len(a):
        if a[i]%2!=0:
            e.append(a[i])
        elif b[i]%2!=0:
            e.append(b[i])
        i+=1
    return e
a=[16,17,18,19,20,23]
b=[1,15,34,56,89,13]
e=[]
def maximum():
    max=0
    j=0
    while j<len(e):
        if e[j]>max:
            max=e[j]
        j+=1
    return max
def main():
    print(odd())
    print(maximum())
main()
# first we find odd number then we find which number is maximum



