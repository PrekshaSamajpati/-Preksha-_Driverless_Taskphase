x = int(input("Type a number of elements: "))
hash_table = [[], [], [], [], [], [], [], [], [], []]
for i in range(x):
    num = int(input("Enter number: "))
    index = num % 10
    low = 0
    high = len(hash_table[index])
    while low < high:
        mid = (low + high) // 2
        if num > hash_table[index][mid]:
            low = mid + 1
        else:
            high = mid
    hash_table[index].insert(low, num)
print("Hash Table:")
for i in range(10):
    print(i, ":", hash_table[i])
