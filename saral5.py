def check_numbers(num1,num2):
    if num1%2==0 and num2%2==0:
        print("dono numbers 2 se divisible hai")
    else:
        print("dono numbers 2 se divisible nahi hai")
num1=int(input("enter any number="))
num2=int(input("enter any number="))
check_numbers(num1, num2)
# here we check both number divisible by 2 or not part1

def check_numbers_list(list1,list2):
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print("same index element even")
        else:
            print("same index element not even")
        i+=1
list1=[2, 6, 18, 10, 3, 75] 
list2=[6, 19, 24, 12, 3, 87]
check_numbers_list(list1, list2)
# here we check same index element ever or not part2
