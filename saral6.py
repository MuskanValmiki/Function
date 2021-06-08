def calculator(number_x, number_y, operation):
    if operation=="add":
        return number_x+number_y
    elif operation=="subtract":
        return number_x-number_y
    elif operation=="multiply":
        return number_x*number_y
    elif operation=="divide":
        return number_x/number_y
number_x=int(input("enter any number="))
number_y=int(input("enter any number="))
operation=input("which operation you want=")
call=calculator(number_x, number_y, operation)
# print(calculator(number_x, number_y, operation))

# part1 we made calculater 

def list_change(call):
    i=0
    multiple_list=[]
    while i<len(list1):
        multiple_list.append(list1[i]*list2[i])
        i+=1
    print(multiple_list)
list1=[5, 10, 50, 20]
list2=[2, 20, 3, 5]
list_change(call)

# by using calculator we find same index multiply part2
