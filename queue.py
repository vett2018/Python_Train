import test_heap


class PriorityQueue: #очередь с приоритетом
    def __init__(self): #экземпляр класса
        self._queue = []
        self._index = 0

    def push(self, item, priority): #экземпляр класса
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self): #экземпляр класса
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


"""
q = PriorityQueue() #присваивание переменной q типа данных очередь, дальше добавляем эементы
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
"""
"""
 q.pop() #удаляет элемент из очереди с наименьшим приоритетом  
"""

