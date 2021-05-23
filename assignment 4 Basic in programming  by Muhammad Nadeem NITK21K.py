list = []
mygradelist = []
rlist = []
operationlist = []
valuelist = []
mylist = []

import statistics  #it is used to import the functions of mean median and mode
import sys
#taking input of names of students
n = int(input("How many students' data you want to enter:  "))
i = 0
k = 0
while i < n:
 for i in range( 0 , n):
    a = str(input("Enter name of student(s to finish): "))
    i += 1
    string = a.upper() #converting lower case into upper case
    list.append(string)
    if a == "s" :
        sys.exit("Exit")
        break
#converting list into tuple
mytupl = tuple(list)

#taking input of grades 
j = 0
while j < n:
 for j in range(0 , n):
    b =int(input("Enter grades of students :\n"))
    j += 1
    if b == "s" :
        sys.exit("Exit") 
        break
    else: mygradelist.append(b)
    
#calculation of formulas
average = sum(mygradelist)/n
maxi = max(mygradelist)
mini = min(mygradelist)
medi = statistics.median(mygradelist)
ch =(input("Do you want to print result? y / n \n"))

if ch == "y" :

    rlist =zip(list, mygradelist)
    for x,y in rlist:
        print(x,y)
    operationlist = ["Average", "Maximum", "Minimum", "Median"]
    valuelist = [average, maxi, mini, medi]
    mylist = zip(operationlist,valuelist)
    for s,t in mylist:
        print(s,t)

else: sys.exit("Exit")
