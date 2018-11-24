def heapsort(arr):
  heaped = Heap()
  sorted_arr = []
  for value in arr:
    heaped.insert(value)
  while heaped.get_size() > 0:
    sorted_arr.append(heaped.delete())
  sorted_arr.reverse()
  return sorted_arr

def heapsort(arr):                                    # Beej's solution
  heap = Heap()                                       # O(1) not passing n here. happens order one time
  sorted = [0] * len(arr)                             # O(n) initialize an array
  for el in arr:                                      # O(n) loop through all the elements
    heap.insert(el)                                   # O(log n) append the value and call bubble up. not O(n) because as we bubble up we dont have to visit every node. only visit the ones that are along the line that traversing from the bottom to the top.
  for i in range(len(arr)):                           # O(n) another loop of order n
    sorted[len(arr) - i - 1] = heap.delete()          # O(log n) appending to the end of the list. heap delete is log n process for the same reason as insert except instead of bubbling up at the bottom, we're sifting down from the top
  return sorted

class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2