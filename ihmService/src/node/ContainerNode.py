from . import Tree

class ContainerNode(Tree.Tree):
    def __init__(self, name, id="null"):
        super().__init__("container")
        self.name = name
        self.id = id

    def generate(self):
        self.generateContent()

        return """
            <div class="container" id="{}">
                <h3>{}</h3>
                {}
            </div>
        """.format(self.id, self.name, self.content)
