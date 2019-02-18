from .node.HeaderNode import HeaderNode
from .node.BodyNode import BodyNode
from .node.HTMLNode import HTMLNode
from .node.HeaderNode import HeaderNode
from .node.ContainerNode import ContainerNode
from .node.InputNode import InputNode
from .node.ButtonNode import ButtonNode
from .node.ToastNode import ToastNode
from .node.JSNode import JSNode
from .node.ChartNode import ChartNode
from .node.FormNode import FormNode


class TreeGenerator():
    def __init__(self):
        self.jsContent = ""

    def generateHeaderNode(self, data):
        return HeaderNode(data['title'])

    def generateBodyNode(self, data):
        bodyNode = BodyNode()
        bodyNode.addChild(ToastNode())

        for container in data:
            bodyNode.addChild(self.generateContainer(container['container']))

        bodyNode.addChild(self.generateJSNode())

        return bodyNode

    def addJavascriptContent(self, content):
        self.jsContent = self.jsContent + content + "\n"

    def generateContainer(self, data):
        if "color" in data:
            containerNode = ContainerNode(data['title'], data['id'], data['color'])
        else:
            containerNode = ContainerNode(data['title'], data['id'])

        for item in data['items']:
            try:
                if "chart" in item:
                    containerNode.addChild(self.generateChartNode(item['chart']))
            except Exception as e:
                print("Osef + " + str(e))

            try:
                if "button" in item:
                    containerNode.addChild(self.generateButtonNode(item['button']))
            except Exception as e:
                print("Osef + " + str(e))

            try:
                if "form" in item:
                    containerNode.addChild(self.generateFormNode(item['form']))
            except Exception as e:
                print("Osef + " + str(e))

        return containerNode

    def generateJSNode(self):
        return JSNode(self.jsContent)

    def generateFormNode(self, data):
        formNode = FormNode(data['buttonText'], data['destination'], data['requestKind'])

        for inputNode in data['items']:
            try:
                formNode.addChild(self.generateInput(inputNode))
            except Exception as e:
                print("A" + str(e))
        return formNode

    def generateButtonNode(self, data):
        if "blockOther" in data:
            print(data['blockOther'])
            buttonNode = ButtonNode(data['buttonText'], data['destination'], data['id'], data['value'], data['autoreload'], data['blockOther'])
        else:
            buttonNode = ButtonNode(data['buttonText'], data['destination'], data['id'], data['value'], data['autoreload'])

        self.addJavascriptContent("updateStateButton(\"{}\");".format(data['id']))

        return buttonNode

    def generateInput(self, data):
        inputNode = InputNode(data['type'], data['description'], data['value'], data['name'])
        return inputNode

    def generateChartNode(self, data):
        chartNode = ChartNode(data['name'], data['yAxe']['min'], data['yAxe']['max'])

        self.addJavascriptContent("generateChart(\"{}\", {}, {});".format(data['name'], data['yAxe']['min'], data['yAxe']['max']))
        return chartNode

    def generate(self, data):
        tree = HTMLNode()

        if data['header']:
            tree.addChild(self.generateHeaderNode(data['header']))
        if data['body']:
            tree.addChild(self.generateBodyNode(data['body']))

        return tree
