from . import Tree

class FormNode(Tree.Tree):
    def __init__(self, buttonText, destination, requestKind):
        super().__init__("form")
        self.buttonText = buttonText
        self.destination = destination
        self.requestKind = requestKind

    def generate(self):
        self.generateContent()

        return """
            <form>
                {}
                <button type="button" class="button-submit" onclick="sendData(this, '{}');">{}</button>
            </form>
        """.format(self.content, self.destination, self.buttonText)
