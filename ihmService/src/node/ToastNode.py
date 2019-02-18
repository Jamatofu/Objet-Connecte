from . import Tree

class ToastNode(Tree.Tree):
    def __init__(self):
        super().__init__("toast")

    def generate(self):
        return """
            <div id="toast-container">
            </div>
        """
