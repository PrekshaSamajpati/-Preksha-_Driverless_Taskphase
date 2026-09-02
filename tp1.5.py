hash_table = [[], [], [], [], [], [], [], [], [], []]
n=int(input("Enter number of elements"))
for i in range(n):
    num = int(input("Enter number: "))

    index = num % 10
    hash_table[index].append(num)
print("Hash Table:")
for i in range(10):
    print(i, ":", hash_table[i])
