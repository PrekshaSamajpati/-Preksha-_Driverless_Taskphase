n = int(input("Enter number of coordinates: "))
list0 = []
list1 = []
list2 = []
print("Enter x coordinate then y coordinate")
for i in range(n):
    ele1 = int(input())
    ele2=int(input())
    list1.append(ele1)
    list2.append(ele2)
for i in range (n):
    print("(", list1[i], ",", list2[i], ")", end=" ")
x=int(input("\nEnter reference x-coordinate: "))
y=int(input("Enter reference y-coordinates: "))
for i in range(n):
    ele3=((list1[i]-x)**2)+((list2[i]-y)**2)
    list0.append(ele3)
for i in range(n):
     for j in range(0, n - i - 1):
         if list0[j] > list0[j + 1]:
            list0[j], list0[j + 1] = list0[j + 1], list0[j]
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
            list2[j], list2[j + 1] = list2[j + 1], list2[j]
for i in range (n):
    print("(", list1[i], ",", list2[i], ")", end=" ")
