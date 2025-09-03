# Basic concept

number = [1, 3, 4, 5, 345,"saroj",bool, 566,]

print(number[5])

number[5] = "kumar" # so list is mutable

print(number[5])
print(number[0:6]) # so list list is also slicing

number.append("Bos")  # append function is add the new data at the end 

print(number)

number1 = [1,2,343,345,45,56,4,] #list of number

number1.sort() # this function is design the list in ascending order
print(number1)

number1.reverse() # this function reverse the list
print(number1)

number1.remove(4)
print(number1)




#Q1. e a program to store a seven fruits in a list inter by suer

fruits = []

f1 = input("Enter the fruits name1= ")
fruits.append(f1)

f2= input("Enter the fruits name2= ")
fruits.append(f2)

f3= input("Enter the fruits name3= ")
fruits.append(f3)

f4= input("Enter the fruits name4= ")
fruits.append(f4)

f5= input("Enter the fruits name5= ")
fruits.append(f5)

f6= input("Enter the fruits name6= ")
fruits.append(f6)

f7= input("Enter the fruits name7= ")
fruits.append(f7)

print(fruits)


