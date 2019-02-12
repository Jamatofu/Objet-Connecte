from . import Tree

class HeaderNode(Tree.Tree):
    def __init__(self, title):
        super().__init__("header")
        self.title = title


    def generate(self):
        style = ""
        js = ""

        with open("style.css", 'r') as f:
            try:
                style = f.read()
            except ex as Exception:
                print(exc)

        with open("chart.js", 'r') as f:
            try:
                js = f.read()
            except ex as Exception:
                print(exc)

        return """
            <head>
                <meta charset="utf-8">
                <title>{}</title>
                <style>{}</style>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.bundle.min.js" type="text/javascript"></script>
                <script>{}</script>
            </head>
            """.format(self.title , style, js)
