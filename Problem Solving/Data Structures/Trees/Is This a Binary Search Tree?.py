""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
import math
def is_bst(root, min_, max_):
    if not root:
        return True
    if root.data < min_ or root.data > max_:
        return False
    return is_bst(root.left, min_, root.data - 1) and is_bst(root.right, root.data + 1, max_)
def check_binary_search_tree_(root):
    return is_bst(root, -math.inf, math.inf)
