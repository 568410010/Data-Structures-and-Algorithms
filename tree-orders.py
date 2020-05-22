# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    #print(self.n)
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    result = []
    root=0
    def inorder(root):
        if self.left[root] != -1:
            inorder(self.left[root])
        result.append(self.key[root])
        if self.right[root] != -1:
            inorder(self.right[root])

    # Finish the implementation
    # You may need to add a new recursive method to do that
    inorder(root)
    #print(result)
    return result

  def preOrder(self):
      result = []
      root = 0

      def preorder(root):
          result.append(self.key[root])
          if self.left[root] != -1:
              preorder(self.left[root])
          if self.right[root] != -1:
              preorder(self.right[root])
      preorder(root)
      return result
    # Finish the implementation
    # You may need to add a new recursive method to do that


  def postOrder(self):
      result = []
      root = 0

      def postorder(root):

          if self.left[root] != -1:
              postorder(self.left[root])
          if self.right[root] != -1:
              postorder(self.right[root])
          result.append(self.key[root])

      postorder(root)
      return result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
