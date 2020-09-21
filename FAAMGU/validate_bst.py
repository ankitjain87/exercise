class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def isValidBST(self, root):
        # using recurssion
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node, lower=float('-inf'), upper=float('inf')):
            
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >=upper:
                return False

            if not check(node.left, lower, val):
                return False
            if not check(node.right, val, upper):
                return False
            return True
        
        return check(root)

    def isValidBST2(self, root):
        # Using stack loop
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop(0)
            if not node:
                continue
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            stack.append((node.left, lower, val))
            stack.append((node.right, val, upper))

        return True

    def isValidBST3(self, root):
        # using inorder traversal
        nums = []
        def in_order(root, nums):
            if root:
                if not in_order(root.left, nums):
                    return False

                if len(nums) == 0:
                    nums.append(root.val)
                else:
                    if root.val <= nums[-1]:
                        return False
                    else:
                        nums.append(root.val)

                if not in_order(root.right, nums):
                    return False
            
            return True
        return in_order(root, nums)

