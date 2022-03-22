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
def main():
  test_list = LinkedList(range(5))
  for e in test_list:
    print(e)
  print(test_list[0])
  test_list[2] = 22
  print(test_list)
if __name__ == "__main__":
  main()