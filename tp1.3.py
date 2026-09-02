class P2:

    def input(self):
        self.x = int(input("Type a number: "))
        self.list = []

        # Take strings as input
        for i in range(self.x):
            ele = input("Enter a string: ")
            self.list.append(ele)

        print("Original list:", self.list)

    def convert(self):
        self.list1 = []

        # Convert strings to lowercase
        for i in range(self.x):
            self.list1.append(self.list[i].lower())

    def sort(self):
        # Selection sort
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
    def binary_search(self):
        search = input("Enter string to search: ")
        search = search.lower()

        low = 0
        high = len(self.list1) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.list1[mid] == search:
                print("String found at index:", mid)
                return

            elif search < self.list1[mid]:
                high = mid - 1

            else:
                low = mid + 1

        print("String not found")
obj = P2()
obj.input()
obj.convert()
obj.sort()
obj.binary_search()

