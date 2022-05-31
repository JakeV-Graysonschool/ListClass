from random import shuffle
from time import thread_time
from statistics import median
class LinkedList:
  
  class __Node:
    
    def __init__(self,item,next=None):
      self.item = item
      self.next = next

    def get_item(self):
      return self.item

    def get_next(self):
      return self.next
      
    def set_item(self,item):
      self.item = item
      
    def set_next(self,next):
      self.next = next
      
  def __init__(self,contents=[]):
    self.first = LinkedList.__Node(None)
    self.last = self.first
    self.num_items = 0
    for e in contents:
      self.append(e)
      
  def append(self,e):
    node = LinkedList.__Node(e)
    self.last.set_next(node)
    self.last = node
    self.num_items += 1

  def __iter__(self):
    cursor = self.first.get_next()
    while cursor != None:
      yield cursor.get_item()
      cursor = cursor.get_next()

  def __str__(self):
    strist = "["
    for e in self:
      strist += str(e) + ","
    strist = strist.rstrip(",")
    strist += "]"
    return strist

  def __getitem__(self,index):
    if 0 <= index < self.num_items:
      cursor = self.first.get_next()
      for i in range(index):
        cursor = cursor.get_next()
      return cursor.get_item()
    raise IndexError("LinkedList index is out of range.")
    
  def __setitem__(self,index,val):
    if 0 <= index < self.num_items:
      cursor = self.first.get_next()
      for i in range(index):
        cursor = cursor.get_next()
      cursor.set_item(val)
      return
    raise IndexError("LinkedList index is out of range.")

  def __contains__(self,val):
    for e in self:
      if e == val:
        return True
    return False

  def __eq__(self,other):
    if type(self) == type(other):
      if self.num_items == other.num_items:
        for e in range(self.num_items):
          if self[e] != other[e]:
            return False
          return True
      return False
    return False
# ^ compare if statement structures v
  def __add__(self,other):
    if type(self) != type(other):
      raise TypeError("Concatenated data are not Linked Lists.")
    super_list = LinkedList()
    for e in self:
      super_list.append(e)
    for e in other:
      super_list.append(e)
    return super_list

  def insert(self,index,item):
    cursor = self.first
    if index < self.num_items:
      for _ in range(index):
        cursor = cursor.get_next()
      new_node = LinkedList.__Node(item,cursor.get_next())
      cursor.set_next(new_node)
      self.num_items += 1
    else:
      raise IndexError("LinkedList index out of range.")

  def __delitem__(self,index):
    cursor = self.first
    print(index)
    print(self.num_items,"-")
    if index < self.num_items:
      for _ in range(index):
        cursor = cursor.get_next()
      new_next = cursor.get_next().get_next()
      cursor.get_next().set_next(None)
      cursor.set_next(new_next)
      self.num_items -= 1
    else:
      raise IndexError("LinkedList index out of range.")

  def __len__(self):
    return self.num_items

  def sorted(self):
    cursor = self.first.get_next()
    for _ in range(self.num_items-1):
      if cursor.get_item() > cursor.get_next().get_item():
        return False
      cursor = cursor.get_next()
    return True

  def swap(self,i,j):
    """t = self[i]
    self[i] = self[j]
    self[j] = t """
    mindex = min(i,j)
    maxdex = max(i,j)
    cursor = self.first.get_next()
    for _ in range(mindex):
      if cursor is not None:
        cursor = cursor.get_next()
    min_node = cursor
    for _ in range(maxdex - mindex):
      if cursor is not None:
        cursor = cursor.get_next()
    max_node = cursor
    temp = min_node.get_item()
    min_node.set_item(max_node.get_item())
    max_node.set_item(temp)
    
  def bubble(self):
    while not self.sorted():
      for i in range(self.num_items-1):
        if self[i] > self[i+1]:
          self.swap(i,i+1)

  def selection(self):
    for i,item in enumerate(self):
      swapdex = self.min_find(i)
      self.swap(i,swapdex)
    return self

  def min_find(self,first=0):
    mindex = first
    minue = self[first]
    for i,item in enumerate(self):
      if i >= mindex and item < minue:
        minue = item
        mindex = i
    return mindex

  def splist(self):
    leng = len(self)
    newst = LinkedList()
    cursor = self.first.get_next()
    for i in range(0,(leng//2)-1):
      cursor = cursor.get_next()
    new_tail = cursor
    cursor = cursor.get_next()
    new_head = cursor
    new_tail.set_next(None)
    self.num_items = leng//2
    newst.first.set_next(new_head)
    newst.num_items = leng - leng//2
    return newst

  def merge(self,self2):
    firststart = self
    secondstart = self2
    cursor1 = firststart.first.get_next()
    cursor2 = secondstart.first.get_next()   
    if cursor2.get_item() < cursor1.get_item():
      self.first.set_item(cursor2)
      self2.fist.set_item(None)
      for i,item in enumerate(secondstart):
        cursor2.get_next()
        
      
  """
    leng = len(firststart)
    old_head = secondstart.first.get_next()
    cursor = firststart.first.get_next()
    for i in range(0,leng-1):
      cursor = cursor.get_next()
    cursor.set_next(old_head)
    self.num_items = leng + len(secondstart)"""
    print(len(self),"len")
    print(self,"+n 2.0")
# ^ misc. shennanigans + additional tomfooleries
  def merge_sort(self):
    if len(self) > 1:
      newst = self.splist()
#      print(self,"/s",newst,"/n")
      newst.merge_sort()
      self.merge_sort()
      self.merge(newst)
    
def test_bubble(n,averages,filename="test_bubble.csv"):
  with open(filename, "w") as f:
    for i in range(2,n+1):
      print(f"Testing Length {i}")
      times_sorted = []
      times_shuffled = []
      times_reversed = []
      times_sortof = []
      for j in range(averages):
        times_sorted.append(timer_bubble(range(i)))
        
        shuffled_list = list(range(i))
        shuffle(shuffled_list)
        times_shuffled.append(timer_bubble(shuffled_list))
#        print(shuffled_list)
        reversed_list = list(range(i,0,-1))
        times_reversed.append(timer_bubble(reversed_list))

        sortish_list = list(range(i))
        swap_sampler = list(range(i))
        shuffle(swap_sampler)
        swap1 = swap_sampler[0]
        swap2 = swap_sampler[1]
        sortish_list[swap1], sortish_list[swap2] = sortish_list[swap2], sortish_list[swap1]
#        print(sortish_list)
        times_sortof.append(timer_bubble(sortish_list))
        
      f.write(f"{i},{median(times_sorted)},{median(times_shuffled)},{median(times_reversed)}, {median(times_sortof)}\n")
      f.flush()
      
def test_selection(n,averages,filename="test_selection.csv"):
  with open(filename, "w") as f:
    for i in range(2,n+1):
      print(f"Testing Length {i}")
      times_sorted = []
      times_shuffled = []
      times_reversed = []
      times_sortof = []
      for j in range(averages):
        times_sorted.append(timer_selection(range(i)))
        
        shuffled_list = list(range(i))
        shuffle(shuffled_list)
        times_shuffled.append(timer_selection(shuffled_list))
#        print(shuffled_list)
        reversed_list = list(range(i,0,-1))
        times_reversed.append(timer_selection(reversed_list))

        sortish_list = list(range(i))
        swap_sampler = list(range(i))
        shuffle(swap_sampler)
        swap1 = swap_sampler[0]
        swap2 = swap_sampler[1]
        sortish_list[swap1], sortish_list[swap2] = sortish_list[swap2], sortish_list[swap1]
#        print(sortish_list)
        times_sortof.append(timer_selection(sortish_list))
        
      f.write(f"{i},{median(times_sorted)},{median(times_shuffled)},{median(times_reversed)}, {median(times_sortof)}\n")
      f.flush()
      
def timer_bubble(normlist):
    linklist = LinkedList(normlist)
    sort_time_sorted = thread_time()
    linklist.bubble()
    return thread_time() - sort_time_sorted
  
def timer_selection(normlist):
    linklist = LinkedList(normlist)
    sort_time_sorted = thread_time()
    linklist.selection()
    return thread_time() - sort_time_sorted
  
def main():
  """
  test_list = LinkedList(range(5))
  twost_list = LinkedList([0,1,22,3,4])
  for e in test_list:
    print(e)
  print(test_list[0])
  test_list[2] = 22
  print(test_list)
  if 31 in twost_list:
    print("True")
  else:
    print("False")
  if test_list == twost_list:
    print("T")
  else:
    print("F")
  print(test_list + twost_list)
  twost_list.insert(3,0)
  del twost_list[4]
  print(twost_list)
  print(len(twost_list))
  print(twost_list.sorted())
  twost_list.swap(0,4)
  print(twost_list)
  twost_list.bubble()
  print(twost_list)
  
  start = thread_time()
  test_bubble(50,3)
  end = thread_time() - start
  print(end)

  
  list1 = LinkedList([5,2,6,7,3])
  sortest = list1.selection()
  print(sortest)
  
  start = thread_time()
  test_selection(200,3)
  end = thread_time() - start
  print(end)
  
  test = LinkedList([1,2,3,4,5,6,7,8,9,10,11])
  new = test.splist()
  print(test)
  print(new)
  """
  mergelistA = LinkedList([1,5,2,6])
  mergelistB = LinkedList([3,4])
  mergelistA.merge_sort()
  print(mergelistA)
if __name__ == "__main__":
  main()