class Tree:
    def __init__(self, kind):
        self.child = []
        self.kind = kind
        self.content = ""

    def addChild(self, node):
        self.child.append(node)

    def isLeaf():
        return not self.child

    def generate(self):
        pass

    def generateContent(self):
        for child in self.child:
            self.content = self.content + child.generate()
