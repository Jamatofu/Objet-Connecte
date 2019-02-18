from . import Tree

class ContainerNode(Tree.Tree):
    def __init__(self, title, id="null", color="green"):
        super().__init__("container")
        self.title = title
        self.id = id
        self.color = color

    def generate(self):
        self.generateContent()

        color = "title-" + self.color

        return """
            <div class="container" id="{}">
                <h3  class="{}">{}</h3>
                {}
            </div>
        """.format(self.id, color, self.title, self.content)
