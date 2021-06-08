def sum():
    print(12+13)
sum() 
# Q1 debug here we miss : 

def welcome():
    print("Welcome to function")
welcome() 
# Q2 debug here we write wrong spelling of def

def isEven():
    if(12%2==0):
        print("Even Number")
    else:
        print("Old Number") 
isEven()
# Q3 debug here we call function before and define later that why it is showing function not define

def greet(*names):
    for name in names:
        print("Welcome", name)
greet("Rinki", "Vishal", "Kartik", "Bijender") 
# Q4 debug here we did not write *

def info(name, age=25):
   print(name + " is " + str(age) + " years old")
info("Sonu")
info("Sana", "17")
info("Umesh", "18") 
# Q5 debug we did not wrote default argument miss str also before age

def studentDetails(name,currentMilestone,mentorName):
    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
studentDetails("Nilam","loop","muskan valmikee") 
# Q6 debug here we did not define mentorName
