class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)

    def displayDescendants(self):
        print('(', end='')
        for c in self.children:
            # Grundlæggende tilfælde:
            print(c.data + ' ', end='')
            # Rekursivt tilfælde:
            c.displayDescendants()
        print(') ', end='')

esther = Node("Esther")
esther.addChild(Node("Bent"))
esther.addChild(Node("Else"))
erna = Node("Erna")
esther.addChild(erna)
lotte = Node("Lotte")
erna.addChild(lotte)
lotte.addChild(Node("Hugo"))
lotte.addChild(Node("Harald"))
esther.displayDescendants()
