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
    t = self[i]
    self[i] = self[j]
    self[j] = t

  def bubble(self):
    while not self.sorted():
      for i in range(self.num_items-1):
        if self[i] > self[i+1]:
          self.swap(i,i+1)

def test_bubble(n,averages):
  for i in range(1,n):
    times_sorted = []
    times_shuffled = []
    for j in range(averages):
      bubblist = list(range(i))
      bubblist = LinkedList(bubblist)
      
      sort_time_sorted = thread_time()
      bubblist.bubble()
      times_sorted.append(thread_time() - sort_time_sorted)
      
      bubblist = list(range(i))
      shuffle(bubblist)
      bubblist = LinkedList(bubblist)
      
      sort_time_shuffled = thread_time()
      bubblist.bubble()
      times_shuffled.append(thread_time() - sort_time_shuffled)
      
    print(f"{i},{median(times_sorted)},{median(times_shuffled)}")
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
  """
  test_bubble(100,3)
if __name__ == "__main__":
  main()