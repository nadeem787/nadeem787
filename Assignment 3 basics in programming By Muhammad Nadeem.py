import statistics
   
#Declare list
mylist = [23, 13, 32, 54, 67, 10, 6, 4, 51, 12, 15, 3]


# calculate the average through sum function
average = sum(mylist)
average = average/12
print("\n The Average of the list through sum function is: ", average)


#calculate the average through for loop
sum = 0
for values in mylist:
    sum = sum + values
    average1 = sum/12
    
print("\n The Average of the list through for loop is: ", average1) 



#calculate the average through mean function
average3 = statistics.mean(mylist)
print("\n The Average of the list through mean function is: ", average3) 



#calculate medain using median function
median = statistics.median(mylist)
print("\n The Median of the list through median function is: ", median) 



#calculate medain without median function
median1 = sorted(mylist)[len(mylist) // 2]
#// means to "divide and round to the next smallest whole number"
print("\n The Median of the list without median function is: ", median1)


#calculate mode using mode function
mode1 = statistics.mode(mylist)
print("\n The Mode of the list using mode function is: ", mode1)
