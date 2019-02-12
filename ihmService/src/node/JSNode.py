from . import Tree

class JSNode(Tree.Tree):
    def __init__(self, content):
        super().__init__("js")
        self.content = content

    def generate(self):
        return """
        <script>
        {}
        </script>""".format(self.content)
