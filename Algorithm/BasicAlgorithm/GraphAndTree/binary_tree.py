class BinTreeNode():
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder(self, s='recursive'):
        def recursive_liner(root):
            return [root.val] + recursive_liner(root.left) + recursive_liner(root.right) if root else []
        if s == 'liner': return recursive_liner(self)

        def recursive(root):
            ans = []
            if not root: return ans

            ans.append(root.val)
            ans.extend(recursive(root.left))
            ans.extend(recursive(root.right))

            return ans
        if s == 'recursive': return recursive(self)

        def nonrecursive(root):
            ans = []
            stack = [root]

            while len(stack) > 0:
                node = stack.pop()
                if not node:
                    continue
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

            return ans

        return nonrecursive(self)

    def postorder(self, s='recursive'):
        def recursive_liner(root):
            return recursive_liner(root.left) + recursive_liner(root.right) + [root.val] if root else []
        if s == 'liner': return recursive_liner(self)

        def recursive(root):
            if not root: return []
            ans = recursive(root.left)
            ans += recursive(root.right)
            ans += [root.val]
            return ans
        if s == 'recursive': return recursive(self)

        def nonrecursive(root):
            if not root: return []
            ans = []
            stack = [root]

            while len(stack) > 0:
                node = stack.pop()
                ans.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            return ans[::-1]

        return nonrecursive(self)

    def inorder(self, s='recursive'):
        def recursive_liner(root):
            return recursive_liner(root.left) + [root.val] + recursive_liner(root.right) if root else []
        if s == 'liner': return recursive_liner(self)

        def recursive(root):
            if not root: return []
            ans = recursive(root.left)
            ans += [root.val]
            ans += recursive(root.right)
            return ans
        if s == 'recursive': return recursive(self)

        def nonrecursive(root):
            if not root: return []
            ans = []
            stack = []

            node = root
            while node:
                stack.append(node)
                node = node.left

            while len(stack) > 0:
                curr = stack.pop()
                ans.append(curr.val)
                node = curr.right
                while node:
                    stack.append(node)
                    node = node.left

            return ans

        return nonrecursive(self)

    def levelorder(self):
        ans = []
        queue = [self]

        while len(queue) > 0:
            node = queue.pop(0)
            ans.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return ans

    def invert(self):
        self.left, self.right = self.right, self.left
        if self.left: self.left.invert()
        if self.right: self.right.invert()

    def is_bst(self):
        def is_bst_node(node, min_val, max_val):
            if not node: return True
            if node.val > max_val or node.val < min_val: return False

            if node.left:
                if not node.left.val <= node.val: return False
                if not is_bst_node(node.left, min_val, min(max_val, node.val)): return False
            if node.right:
                if not node.right.val >= node.val: return False
                if not is_bst_node(node.right, max(min_val, node.val), max_val): return False

            return True

        return is_bst_node(self, float('-inf'), float('inf'))

    def is_full(self):
        count = self.count()
        depth = self.depth()

        return count == 2 ** (depth + 1) - 1

    def is_complete(self):
        """ go through the tree level by level
        if visited a None node, all the rest unvisited nodes should be None"""
        queue = [self]

        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
            else:
                while len(queue) > 0:
                    restNode = queue.pop(0)
                    if restNode is not None:
                        return False
        return True

    def is_balanced(self):
        depth_l, depth_r = -1, -1
        is_bal_l, is_bal_r = True, True
        if self.left:
            depth_l = self.left.depth()
            is_bal_l = self.left.is_balanced()
        if self.right:
            depth_r = self.right.depth()
            is_bal_r = self.right.is_balanced()

        return is_bal_l and is_bal_r and abs(depth_l - depth_r) <= 1

    def count(self):
        c = 1
        if self.left: c += self.left.count()
        if self.right: c += self.right.count()
        return c

    def leaf_count(self, s='recursive'):
        def recursive(root):
            if not root: return 0
            if root.left is None and root.right is None: return 1
            return recursive(root.left) + recursive(root.right)
        if s == 'recursive': return recursive(self)

        def nonrecursive(root):
            queue = [root]
            count = 0
            while len(queue) > 0:
                node = queue.pop()
                if node.left is None and node.right is None:
                    count += 1
                else:
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            return count
        return nonrecursive(self)

    def depth(self, level = 0):
        # root level depth == 0
        level_left = self.left.depth(level + 1) if self.left else level
        level_right = self.right.depth(level + 1) if self.right else level

        return max(level_left, level_right)
