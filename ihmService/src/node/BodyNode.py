from . import Tree

class BodyNode(Tree.Tree):
    def __init__(self):
        super().__init__("body")

    def generate(self):
        self.generateContent()

        return """
            <body>
            {}
            </body>
        """.format(self.content)
