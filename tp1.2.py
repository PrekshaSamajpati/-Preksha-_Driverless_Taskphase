class P2:
    def input(self):
        self.x = int(input("Type a number: "))
        self.list = []
        for i in range(self.x):
            ele = input("Enter a string: ")
            self.list.append(ele)
        print("Original list:", self.list)
    def convert(self):
        self.list1 = []
        for i in range(self.x):
            self.list1.append(self.list[i].lower())
    def sort(self):
        n = len(self.list1)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.list1[j] < self.list1[min_index]:
                    min_index = j
            # Swap
            self.list1[i], self.list1[min_index] = \
                self.list1[min_index], self.list1[i]
            self.list[i], self.list[min_index] = \
                self.list[min_index], self.list[i]

        print("Sorted list:", self.list)
obj = P2()
obj.input()
obj.convert()
obj.sort()
