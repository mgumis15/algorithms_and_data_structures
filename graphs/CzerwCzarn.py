
import math
# ? <CORE>


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = True

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
        current = new
        while current.parent and current.parent.color:
            itemParent = current.parent
            if itemParent.parent:
                grandParent = itemParent.parent
            else:
                break
            if itemParent == grandParent.left and grandParent.left.color:
                itemParent.color = False
                grandParent.left.color = False
                grandParent.color = True
                current = grandParent
                continue


def printBST(root, dir=None):
    if root.parent:
        print(root.parent.key, "-", dir, "->", root.key)
    else:
        print("Root: ", root.key)
    if root.right:
        printBST(root.right, "R")
    if root.left:
        printBST(root.left, "L")
# ? </CORE>


root = BSTNode(20)
root.color = False
root.add(10)
root.add(27)
root.add(15)
root.add(13)
root.add(5)
root.add(27)
root.add(22)
root.add(30)
root.add(28)
root.add(35)
root.add(40)
