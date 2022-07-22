# CTI-110
# P2HW2 - List and Sets
# Your Name 
# Date
#

mylist = []
num = float(input("Enter number 1: "))
mylist.append(num)
num = float(input("Enter number 2: "))
mylist.append(num)
num = float(input("Enter number 3: "))
mylist.append(num)
num = float(input("Enter number 4: "))
mylist.append(num)
num = float(input("Enter number 5: "))
mylist.append(num)
num = float(input("Enter number 6: "))
mylist.append(num)
print("\nCreated list: \n", mylist)


smallest = (min(mylist))
print("Smallest number in list: ", smallest)
print("Largest number in list: ", max(mylist))
print("Sum of numbers in list: ", sum(mylist))
print("Average of all numbers in list: ", sum(mylist)/len(mylist))
print("\nCreated set: ")
print(set(mylist))


