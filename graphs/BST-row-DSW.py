
import math
# ? <CORE>


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

# Rotacja w prawo


def rot_R(root):
    if not root.left:
        return None
    B = root.left
    B.parent, root.parent = root.parent, B
    B.right, root.left = root, B.right
    if root.left:
        root.left.parent = root
    if B.parent:
        B.parent.right = B
    return B


# Rotacja w lewo

def rot_L(root):
    if not root.right:
        return None
    B = root.right
    B.parent, root.parent = root.parent, B
    B.left, root.right = root, B.left
    if root.right:
        root.right.parent = root
    if B.parent:
        B.parent.right = B
    return B

# Algorytm DSW


def DSW(root, n):
    current = root
    # Pierwsza część algorytmu przetwarza drzewo w postać listy biegnącej caly czas w prawo, poprzez obroty w prawo wszystkich elementów posiadających lewe dzieci
    while current.left:
        rot_R(current)
        current = current.parent
        head = current
    while current:
        if current.left:
            rot_R(current)
            current = current.parent
        else:
            current = current.right
    printBST(head)

    # Druga część przekształca tak utworzoną listę w zbalansowane drzewo za pomocą obrotów w lewo.Obracamy co drugi węzeł. Wyznaczamy również liczbę obrotów daną wzorem 2^(floor(log2(n+1)))
    current = head
    m = pow(2, math.floor(math.log2(n+1)))-1
    head = rotate(current, n-m)
    print(n, m)
    while m > 1:
        m /= 2
        head = rotate(head, m)
        # m /= 2

    printBST(head)


def rotate(root, count):
    gp = None
    current = root
    head = root
    if current.right:
        child = current.right
        if current.parent == None:
            head = current.right
    while count > 0 and current and current.right:
        if child != None:
            rot_L(current)
            gp = child
            current = gp.right
            if current:
                child = current.right
            else:
                child = None
        else:
            break
        count -= 1
    return head


# root = BSTNode(20)
# root.add(10)
# root.add(27)
# root.add(15)
# root.add(13)
# root.add(5)
# root.add(22)
# root.add(30)
# root.add(28)
# root.add(35)
# root.add(40)
# DSW(root, 11)

root = BSTNode(9)
root.add(5)
root.add(15)
root.add(7)
root.add(10)
root.add(18)
root.add(19)
DSW(root, 7)
