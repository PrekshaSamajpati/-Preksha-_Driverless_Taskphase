n=int(input("enter the number of strings: "))
string_list=[]
for i in range(n):
    user_string=input(f"enter string:{i+1}")
    string_list.append(user_string)
alphabet_counts={}
for word in string_list:
    word=word.lower()
    for char in word:
        if char.isalpha():
            if char in alphabet_counts:
                alphabet_counts[char] += 1
            else:
                alphabet_counts[char] = 1
print(alphabet_counts)
