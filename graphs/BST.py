
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def find(self, key):
        while self != None:
            if self.key == key:
                return self
            elif key < self.key:
                self = self.left
            else:
                self = self.right
        return None

    def add(self, key):
        new = BSTNode(key)
        while True:
            if key >= self.key:
                if self.right != None:
                    self = self.right
                else:
                    new.parent = self
                    self.right = new
                    break
            else:
                if self.left != None:
                    self = self.left
                else:
                    new.parent = self
                    self.left = new
                    break

    def fMax(self):
        while self.right != None:
            self = self.right
        return self

    def fMin(self):
        while self.left != None:
            self = self.left
        return self


def printBST(root, dir=None):
    if root.parent:
        print(root.parent.key, "-", dir, "->", root.key)
    else:
        print("Root: ", root.key)
    if root.right:
        printBST(root.right, "R")
    if root.left:
        printBST(root.left, "L")
