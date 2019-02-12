from . import Tree

class HTMLNode(Tree.Tree):
    def __init__(self):
        super().__init__("html")

    def generate(self):
        self.generateContent()

        return """
        <!DOCTYPE html>
        <html>
            {}
        </html>
        """.format(self.content)
