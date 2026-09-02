m1 = int(input("Type row of first matrix: "))
n1 = int(input("Type column of first matrix: "))
m2 = int(input("Type row of second matrix: "))
n2 = int(input("Type column of second matrix: "))
if m2 != n1:
    print("Matrix multiplication cannot be supported")
    exit()
arr1 = []
arr2 = []
arr = []
print("Input elements of first matrix")
for i in range(m1):
    row = []
    for j in range(n1):
        ele1 = int(input())
        row.append(ele1)
    arr1.append(row)
for row in arr1:
    print(row)
print("Input elements of second matrix")
for i in range(m2):
    row = []
    for j in range(n2):
        ele2 = int(input())
        row.append(ele2)
    arr2.append(row)
for row in arr2:
    print(row)
for i in range(m1):
    row = []
    for j in range(n2):
        row.append(0)
    arr.append(row)
# Matrix multiplication
for i in range(m1):          # rows of first matrix
    for j in range(n2):      # columns of second matrix
        for k in range(n1):  # common dimension
            arr[i][j] += arr1[i][k] * arr2[k][j]
print("Result matrix:")
for row in arr:
    print(row)
