class QueuePriorites:
    def __init__(self, lst):
        self.lst = lst
        self.build_max_h()

    def max_h(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        largest = left if left < len(self.lst) and self.lst[i] < self.lst[left] else i
        largest = right if right < len(self.lst) and self.lst[largest] < self.lst[right] else largest

        if i != largest:
            self.lst[i], self.lst[largest] = self.lst[largest], self.lst[i]
            self.max_h(largest)
    
    def build_max_h(self):
        for i in range(int(len(self.lst) / 2), -1, -1):
            self.max_h(i)

    def __str__(self):
        result = 'QueuePriorites: ['
        for number in self.lst:
            result += str(number) + ', '
        result += ']'

        return result
    
    def extract_max(self):
        self.lst[0], self.lst[-1] = self.lst[-1], self.lst[0]
        result = self.lst.pop()
        self.max_h(0)

        return result
    
    def maximum(self):
        return self.lst[0]
    
    def insert(self, x):
        self.lst.append(x)
        i = len(self.lst) - 1
        parent_i = int(i / 2)
        while i > -1 and self.lst[i] > self.lst[parent_i]:
            self.lst[i], self.lst[parent_i] = self.lst[parent_i], self.lst[i]
            i = parent_i
            parent_i = int(i / 2)
        


if __name__ == '__main__':
    lst = [3, 2, 1, 4, 6, 87, 7]
    queue = QueuePriorites(lst)
    print(queue)
    queue.insert(100)
    queue.insert(43)
    queue.insert(13)
    print(queue)

    