from . import Tree

class ChartNode(Tree.Tree):
    def __init__(self, name, minValue, maxValue):
        super().__init__("chart")
        self.name = name
        self.minValue = minValue
        self.maxValue = maxValue

    def generate(self):
        return """
            <canvas id="{}" width="100%" height="100%"></canvas>
        """.format(self.name)
