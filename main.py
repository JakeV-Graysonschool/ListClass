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
    
def main():
  test_list = LinkedList([1,2,3])
  print(test_list)
if __name__ == "__main__":
  main()