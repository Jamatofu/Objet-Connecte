from . import Tree

class InputNode(Tree.Tree):
    def __init__(self, kind, description, value, name):
        super().__init__("input")
        self.type = kind
        self.description = description
        self.value = value
        self.name = name

    def generate(self):
        return """
            <label for="{}">{}<input type="{}" value="{}" name="{}"></label>
        """.format(self.name, self.description, self.kind, self.value, self.name)
