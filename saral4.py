def add_numbers(num1,num2):
    print(num1+num2)
num1=int(input("enter any number="))
num2=int(input("entr any number="))
add_numbers(num1, num2)
# here we print sum of two numbers part1

def add_numbers_list(list1,list2):
    i=0
    list=[]
    while i<len(list1):
        list.append(list1[i]+list2[i])
        i+=1
    print(list)
add_numbers_list([50, 60, 10],[10, 20, 13])
# same index element sum part2
