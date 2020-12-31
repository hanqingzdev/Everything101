import unittest
from unittest_data_provider import data_provider
import random
from binary_tree import BinTreeNode
import binarytree as bt

def buildData(values=None, height=None, perfect=False):
    if values:
        btTree = bt.build(values)
    elif height:
        btTree = bt.tree(height=height, is_perfect=perfect)
    else:
        btTree = None

    def convert(btTree):
        if not btTree: return None
        values = btTree.values
        nodes = [BinTreeNode(values.pop(0))]
        root = nodes[0]

        while len(values) > 0:
            parent = nodes.pop(0)
            left = BinTreeNode(values.pop(0))
            right = BinTreeNode(values.pop(0) if len(values) > 0 else None)
            nodes.append(left)
            nodes.append(right)
            if parent and parent.val is not None:
                if left.val is not None: parent.left = left
                if right.val is not None: parent.right = right

        return root

    return (btTree, convert(btTree))


data = lambda : (
    buildData(list(range(1, 2**3))),
    buildData(list(range(1, 2**4))),
    buildData(list(range(1, 2**4+5))),
    buildData([1,2,3,None, None,6,7,None,None,None,None,12,13]),
    buildData([5,3,10,0,None,6,None,None,None,None,None,None,8,None,None]),
    buildData([5,3,10,0,None,6,None,None,None,None,None,4,8,None,None]),
    buildData([5,3,10,0,7,6,None,None,None,None,None,None,8,None,None]),
    buildData(height=5),
    buildData(height=9),
    buildData(height=2),
    buildData(height=2, perfect=True),
    buildData(height=9, perfect=True),
)

class BinTreeTest(unittest.TestCase):
    @data_provider(data)
    def test_preorder(self, btRoot, tree):
        expected = [e.value for e in btRoot.preorder]
        for alg in ['liner', 'recursive', 'nonrecursive']:
            self.assertEqual(expected, tree.preorder(alg), "Alogrithm: %s \n %s" % (alg, str(btRoot)))

    @data_provider(data)
    def test_postorder(self, btRoot, tree):
        expected = [e.value for e in btRoot.postorder]
        for alg in ['liner', 'recursive', 'nonrecursive']:
            self.assertEqual(expected, tree.postorder(alg), "Alogrithm: %s \n %s" % (alg, str(btRoot)))

    @data_provider(data)
    def test_inorder(self, btRoot, tree):
        expected = [e.value for e in btRoot.inorder]
        for alg in ['liner', 'recursive', 'nonrecursive']:
            self.assertEqual(expected, tree.inorder(alg), "Alogrithm: %s \n %s" % (alg, str(btRoot)))

    @data_provider(data)
    def test_levelorder(self, btRoot, tree):
        expected = [e.value for e in btRoot.levelorder]
        self.assertEqual(expected, tree.levelorder(), btRoot)

    @data_provider(data)
    def test_invert(self, btRoot, tree):
        expected = [e.value for e in btRoot.inorder][::-1]
        tree.invert()
        self.assertEqual(expected, tree.inorder(), btRoot)

    @data_provider(data)
    def test_is_bst(self, btRoot, tree):
        self.assertEqual(btRoot.is_bst, tree.is_bst(), btRoot)

    @data_provider(data)
    def test_is_full(self, btRoot, tree):
        self.assertEqual(btRoot.is_perfect, tree.is_full(), btRoot)

    @data_provider(data)
    def test_is_complete(self, btRoot, tree):
        self.assertEqual(btRoot.is_complete, tree.is_complete(), btRoot)

    @data_provider(data)
    def test_is_balanced(self, btRoot, tree):
        self.assertEqual(btRoot.is_balanced, tree.is_balanced(), btRoot)

    @data_provider(data)
    def test_count(self, btRoot, tree):
        self.assertEqual(btRoot.size, tree.count(), btRoot)

    @data_provider(data)
    def test_leaf_count(self, btRoot, tree):
        for alg in ['recursive', 'nonrecursive']:
            self.assertEqual(btRoot.leaf_count, tree.leaf_count(alg), "Alogrithm: %s \n %s" % (alg, str(btRoot)))

    @data_provider(data)
    def test_depth(self, btRoot, tree):
        self.assertEqual(btRoot.height, tree.depth(), btRoot)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BinTreeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
