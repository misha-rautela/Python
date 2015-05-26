class Node:
  def __init__(self,val,nxt):
    self.val = val
    self.nxt = nxt
 
def prnt(n):
  print n.val
  nxt =n.nxt
  if(nxt is not None):
    prnt(nxt)
 
#Reverse
def reverse_list(n,last):
  if n is None:
    return last
  nxt = n.nxt
  n.nxt = last
  return reverse_list(nxt, n)
 
 
n0 = Node('A',None)
n1 = Node('B',n0)
n2 = Node('C',n1)
n3 = Node('D',n2)
 
prnt(n3)
result = reverse_list(n3, None)
prnt(result)

