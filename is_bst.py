#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  if not tree: return True
  minV, maxV=-pow(2, 31), pow(2, 31)-1

  def inorder(root):
    v, l, r = root
    nonlocal minV
    nonlocal maxV
    if l!=-1:
      if not inorder(tree[l]):
        return False
    if not minV< v < maxV: return False
    minV=v
    if r!=-1:
      if not inorder(tree[r]):
        return False
    return True

  return inorder(tree[0])






def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
