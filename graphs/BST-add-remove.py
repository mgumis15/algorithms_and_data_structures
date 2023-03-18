# Mateusz Mazur
# Funkcja insert działa w czasie O(logn), ponieważ poszukuje w głąb drzewa miejsca, gdzie powinna się znaleźć dodawana liczba, jeżeli ją znajdzie, zwraca False, jeżeli jej nie znajdzie, to ją dodaje.
# Funkcja remove dzieli się na trzy przypadki:
# I - usuwany element jest liściem bez potomków, więc tylko go usuwamy
# II - usuwany element ma tylko jednego potomka, więc przepinamy potomka w miejsce usuwanego elementu
# III - usuwany element ma dwoje dwoje potomków, więc znjadujemy jego następnik (minimum z jego prawego poddrzewa), odpowiednio usuwając ten ten następnik (i przepinając jego dzieci), a wartość key usuwanego elementu zamieniamy na key następnika
# Złożoność to O(logn)
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

# Funkcja dodająca


def insert(root, key):
    new = BSTNode(key)
    # Jeżeli drzewo jest puste, to dodajemy (przez wymogi zadania nie mogę zwrócić adresu nowego 'roota', ale normalnie bym to zrobił")
    if root == None:
        root = new
        return True
    current = root
    # Przeszukiwanie wgłąb drzewa
    while True:
        if current.key == key:
            return False
        elif current.key < key:
            if current.right != None:
                current = current.right
            else:
                new.parent = current
                current.right = new
                return True
        else:
            if current.left != None:
                current = current.left
            else:
                new.parent = current
                current.left = new
                return True


def remove(root, key):
    # Funkcja znajdująca szukany element
    def find(root, key):
        while root != None:
            if root.key == key:
                return root
            elif root.key > key:
                root = root.left
            else:
                root = root.right
        return None
    # Funkcja znajdująca następnik elementu o danej wartości key

    def findNext(root, key):
        if root.right:
            right = root.right
            while right.left != None:
                right = right.left
            return right
        else:
            last = root
            root = root.parent
            while root:
                if root.left == last:
                    return root
                else:
                    last = root
                    root = root.parent
            return None

    curr = find(root, key)
    if not curr:
        return False

    if curr.left == None and curr.right == None:
        # I przypadek
        if curr.parent != None:
            if curr.parent.right == curr:
                curr.parent.right = None
            else:
                curr.parent.left = None
        else:
            curr = None
    else:
        # II przypadek
        if curr.left == None:
            if curr.parent != None:
                if curr.parent.right == curr:
                    curr.parent.right = curr.right
                else:
                    curr.parent.left = curr.right
                curr.right.parent = curr.parent
            else:
                # Przypadek, gdy usuwamy root'a z jednym dzieckiem
                pom = curr.right
                curr.key = pom.key
                curr.right = pom.right
                curr.left = pom.left

        elif curr.right == None:
            if curr.parent != None:
                if curr.parent.right == curr:
                    curr.parent.right = curr.left
                else:
                    curr.parent.left = curr.left
                curr.left.parent = curr.parent
            else:
                pom = curr.left
                curr.key = pom.key
                curr.right = pom.right
                curr.left = pom.left
        else:
            # III przypadek
            next = findNext(curr, curr.key)
            if next.parent.right == next:
                next.parent.right = next.right
            else:
                next.parent.left = next.right
            if next.right != None:
                next.right.parent = next.parent
            curr.key = next.key
    return True
