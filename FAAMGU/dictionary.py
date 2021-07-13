
class LinkedList:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None
    self.index = 0, 1, 2


  def add_node():
    pass

  def delete():
    pass

class HashMap:
  def __init__(self, size):
    self.bucket_size = size
    self.array = [None] * self.bucket_size

  def get_position(self, key):
    i = hash(key)
    return i % len(self.array)


  def put(self, key, val):
    pass


  def add(self, key, val):
    ind = self.get_position(key)
    if not self.array[ind]:
      l = LinkedList(key, val)
      self.array[ind] = l
    else:
      l = self.array[ind]
      prev = None
      while l != None:
        if l.key == key:
          l.val = val
          return

        prev = l
        l = l.next

      prev.next = LinkedList(key, val)

    return True


  def delete(self, key):
    ind = self.get_position(key)
    if not self.array[ind]:
      return None

    l = self.array[ind]

    if l.key == key:
      self.array[ind] = l.next
      return

    prev = None
    while l:
      if l.key == key:
        prev.next = l.next
        if l.next:
          l.next.prev = prev

        return

      prev = l
      l = l.next

    return None

  
  def get(self, key):
    ind = self.get_position(key)
    if not self.array[ind]:
      return None

    l = self.array[ind]
    while l:
      if l.key == key:
        return l.val
      l = l.next

    return None



# hm = HashMap(size=1)
# hm.add('a', 1)
# print(hm.get('a'))
# hm.add('b', 2)
# print(hm.get('a'))
# hm.add('c', 3)
# hm.add('d', 4)
# hm.delete('a')
# print("---delete---", hm.get('a'))
# hm.delete('d')
# print("----delete---", hm.get('d'))

# print(hm.array)




# class LinkedHashMap:
#   def __init__():
#     self.linkedList = LinkedList()
#     self.linkedMap = HashMap()


#   def add(self, key):
#     if key
