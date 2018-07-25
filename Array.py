class Array:
    def __init__(self, *args):
        self.arr = []
        for arg in args:
            self.arr.append(arg)
    
    def push(self, value):
        self.arr.append(value)

    def get_array(self):
        return self.arr

    def heap_sort(self):
        """ Классический алгоритм пирамидальной сортировки. Работает за время O(nlogn) в любом случае.
            Константа там чуть больше, чем, например в быстрой сортировке, но зато даже для худшего случая 
            работает за O(nlogn), тогда как быстрая сортировка в худшем случае работает за 0(n^2) (в теории).
            Также алгоритм не требует дополнительной памяти. Я реализовал его с использоваением дополнительной
            памяти O(n) (создается новый массив temp_arr размером n). 
        """
        temp_arr = []
        self.build_max_h()

        for i in range(len(self.arr) - 1, -1, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            temp_arr.append(self.arr.pop(i))
            self.max_h(0)
        self.arr = temp_arr[::-1]        

    def max_h(self, i):
        l = 2 * i + 1
        r = 2 * i + 2

        largest = l if l < len(self.arr) and self.arr[i] < self.arr[l] else i
        largest = r if r < len(self.arr) and self.arr[largest] < self.arr[r] else largest

        if i != largest:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_h(largest)

    def build_max_h(self):
        for i in range(int(len(self.arr) / 2), -1, -1):
            self.max_h(i)


if __name__ == '__main__':
    array = Array(5, 6, 3, 2, 1)
    array.push(4)
    print('До сортировки:', array.get_array())
    array.heap_sort()
    print('После сортировки:', array.get_array())


