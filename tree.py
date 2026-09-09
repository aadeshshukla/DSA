# Tree data structure
# tree is a hierarchical data structure that consists of nodes connected by edges.
#  Each node contains a value and may have child nodes.
#  The topmost node is called the root, and nodes with no children are called leaves. 
# Trees are used in various applications such as file systems, databases, and algorithms.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# leetcode problems on trees

# 1) Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).
# example:
# Given binary tree [3,9,20,null,null,15,7],
# return its level order traversal as: [[3], [9,20], [15,7]]

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level_values = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level_values.append(node.value)
            queue.extend(node.children)
        
        result.append(level_values)
    
    return result

    