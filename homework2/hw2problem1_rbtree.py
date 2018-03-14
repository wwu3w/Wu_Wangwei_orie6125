""""Problem1: Implementation of Red Black tree as a class"""

black = "black"
red = "red"


class rbnode:

    def __init__(self, key, color=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color


class rbtree:
    null_leaf = rbnode(key=None)

    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if x.right is not None:
            x.right.parent = y
        y.parent = x.parent
        if (x.parent is None):
            self.root = y
        elif (x == x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if (x.left is not None):
            x.left.parent = y
        y.parent = x.parent
        if (x.parent is None):
            self.root = y
        elif (x == x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def _insert(self, new_key):
        new = rbnode(new_key, color=red)
        y = None
        r = self.root
        while (r != None):
            y = r
            if (new.key < r.key):
                r = r.left
            else:
                r = r.right
        new.parent = y
        if (y is None):
            self.root = new
        elif (new.key < y.key):
            y.left = new
        else:
            y.right = new

        self._reblance(new)

    def _remove(self, key):
        x = self._find_node(key)
        if x is None:  # node is not in the tree
            return
        self._node_remove(x)

    def _reblance(self, new):

        while (new != self.root and new.parent.color == red):
            if (new.parent == new.parent.parent.left):
                y = new.parent.parent.right
                if (y.color == red):
                    new.parent.color = black
                    y.color = black
                    new.parent.parent.color = red
                    new = new.parent.parent
                else:
                    if (new == new.parent.right):
                        new = new.parent
                        self._left_rotate(new)
                    new.parent.color = black
                    new.parent.parent.color = red
                    self._right_rotate(new.parent.parent)
            else:
                y = new.parent.parent.left
                if (y.color == red):
                    new.parent.color = black
                    y.color = black
                    new.parent.parent.color = red
                    new = new.parent.parent
                else:
                    if (new == new.parent.right):
                        new = new.parent
                        self._right_rotate(new)
                    new.parent.color = black
                    new.parent.parent.color = red
                    self._left_rotate(new.parent.parent)
        self.root.color = black

    def _node_remove(self, x):
        if (x.right != None and x.left != None):
            successor = self._find_in_order_successor(x)
            x.value = successor.value  # switch the value
            self._node_remove(successor)
        elif (x.right == None):
            xp = x.parent
            xl = x.left
            if (x == xp.left):
                xp.left = xl
            else:
                xp.right = xl
            if (xl != None):
                xl.parent = xp
                if x.color == black:
                    xl.color = black
        else:  # r.right != none and r.left == None
            xp = x.parent
            xr = x.right
            if (x == xp.left):
                xp.left = xr
            else:
                xp.right = xr
            xr.parent = xp
            if x.color == black:
                xr.color = black

    def _find_node(self, key):
        def _inner_find(r):
            if (r is None or r == self.null_leaf):
                return None
            if key > r.key:
                return _inner_find(r.right)
            elif key < r.key:
                return _inner_find(r.left)
            else:
                return r

        found_node = _inner_find(self.root)
        return found_node

    def _find_in_order_successor(self, x):
        y = x.right.left
        if (y == None):
            return x.right
        while (y.left != None):
            y = y.left
        return y

    def _tree_minimum(self, x):
        while (x.left != None):
            x = x.left
        return x

    def _tree_maximum(self, x):
        while (x.right != None):
            x = x.right
        return x
