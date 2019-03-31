# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/2/23 20:37
@description:
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

"""
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def maxDepth(root):
    stack = []
    if root is not None:
        stack.append((1,root))
    depth = 0
    while stack != []:
        current_depth,root = stack.pop()
        if root is not None:
            depth = max(depth,current_depth)
            stack.append((current_depth+1,root.left))
            stack.append((current_depth+1,root.right))
    return depth