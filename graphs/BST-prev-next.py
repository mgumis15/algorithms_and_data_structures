# 1.Zaimplementuj znajdowanie następnika i poprzednika elementu w drzewie bst
# 2. Zaproponuj w jaki sposób znaleźć maksymalny przepływ w sieci, w której możliwe jest kilka ujść i kilka źródeł

from bst import BSTNode


def findNext(root, key):
    curr = root.find(key)
    if curr.right:
        return curr.right.fMin().key
    else:
        last = curr
        curr = curr.parent
        while curr:
            if curr.left == last:
                return curr.key
            else:
                last = curr
                curr = curr.parent
        return None


def findPrev(root, key):
    curr = root.find(key)
    if curr.left:
        return curr.left.fMax().key
    else:
        last = curr
        curr = curr.parent
        while curr:
            if curr.right == last:
                return curr.key
            else:
                last = curr
                curr = curr.parent
        return None


def printBST(root, dir=None):
    if root.parent:
        print(root.parent.key, "-", dir, "->", root.key)
    else:
        print("Root: ", root.key)
    if root.right:
        printBST(root.right, "R")
    if root.left:
        printBST(root.left, "L")


root = BSTNode(20)
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


printBST(root)
# root = BSTNode(9)
# root.add(5)
# root.add(15)
# root.add(4)
# root.add(7)
# root.add(10)
# root.add(18)
# root.add(1)
# root.add(6)
# root.add(8)
# root.add(12)
# root.add(19)


print(findPrev(root, 5))


# AD 2
# dodajemy dwa wierzchołki, superujście i superźródło, i łączymy wszystkie ujścia z superujściem krawędziami o nieskończonej przepustowości i tak samo w przypadku superźródła
