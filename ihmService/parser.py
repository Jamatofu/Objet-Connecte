#!/usr/bin/python
# coding: utf-8

import yaml

data = []

class Tree:
    def __init__(self, kind):
        self.child = []
        self.kind = kind

    def addChild(self, node):
        self.child.append(node)

    def isLeaf():
        return not self.child

class HeaderNode(Tree):
    def __init__(self, title):
        super().__init__("header")
        self.title = title

class BodyNode(Tree):
    def __init__(self):
        super().__init__("body")

class ContainerNode(Tree):
    def __init__(self, name):
        super().__init__("container")
        self.name = name

class FormNode(Tree):
    def __init__(self, buttonText, destination, requestKind):
        super().__init__("form")
        self.buttonText = buttonText
        self.destination = destination
        self.requestKind = requestKind

class ButtonNode(Tree):
    def __init__(self, buttonText, destination, name, value):
        super().__init__("button")
        self.buttonText = buttonText
        self.destination = destination
        self.name = name
        self.value = value

class ChartNode(Tree):
    def __init__(self, name, minValue, maxValue):
        super().__init__("chart")
        self.name = name
        self.minValue = minValue
        self.maxValue = maxValue

class JSNode(Tree):
    def __init__(self, content):
        super().__init__("js")
        self.content = content

class InputNode(Tree):
    def __init__(self, kind, description, value, name):
        super().__init__("input")
        self.type = kind
        self.description = description
        self.value = value
        self.name = name

class ToastNode(Tree):
    def __init__(self):
        super().__init__("toast")

def generateHTML(content):
    return """
    <!DOCTYPE html>
    <html>
        {}
    </html>
    """.format(content)

def generateHeader(title):
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
        """.format(title, style, js)

def generateContainer(content, title):
    return """
        <div class="container">
            <h3>{}</h3>
            {}
        </div>
    """.format(title, content)

def generateForm(redirection, requestKind, content, buttonText):
    return """
        <form action="{}" method="{}">
            {}
            <button type="button" class="button-submit" onclick="sendData(this);">{}</button>
        </form>
    """.format(redirection, requestKind, content, buttonText)

def generateBody(content):
    return """
        <body>
        {}
        </body>
    """.format(content)

def generateInput(kind, description, value, name):
    return """
        <label for="{}">{}<input type="{}" value="{}" name="{}"></label>
    """.format(name, description, kind, value, name)


def generateButton(buttonText, destination, name, value):
    return """
        <button type="button" id="{}" class="button-click" onclick="updateActionneur('{}', '{}')">{}</button>
    """.format(name, destination, value, buttonText)

def generateChart(name, minValue, maxValue):
    return """
        <canvas id="{}" width="100%" height="100%"></canvas>
    """.format(name)

def generateJs(content):
    return """
    <script>
    {}
    </script>""".format(content)

def generateInput(kind, description, value, name):
    return """
        <label for="{}">{} : </label><input type="{}" value="{}" name="{}">
    """.format(name, description, kind, value, name)

def generateToast():
    return """
        <div id="toast-container">
        </div>
    """

def generateTree(tree):
    if not tree:
        return

    content = ""

    if tree.child:
        for child in tree.child:
            content = content + generateTree(child)

    kindTree = tree.kind

    if kindTree == "html":
            return generateHTML(content)
    elif kindTree == "header":
        return generateHeader("titre")
    elif kindTree == "body":
        return generateBody(content)
    elif kindTree == "container":
        return generateContainer(content, tree.name)
    elif kindTree == "form":
        return generateForm(tree.destination, tree.requestKind, content, tree.buttonText)
    elif kindTree == "button":
        return generateButton(tree.buttonText, tree.destination, tree.name, tree.value)
    elif kindTree == "chart":
        return generateChart(tree.name, tree.minValue, tree.maxValue)
    elif kindTree == "js":
        return generateJs(tree.content)
    elif kindTree == "input":
        return generateInput(tree.type, tree.description, tree.value, tree.name)
    elif kindTree == "toast":
        return generateToast()

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
        containerNode = ContainerNode(data['name'])

        for item in data['items']:
            try:
                if item['chart']:
                    containerNode.addChild(self.generateChartNode(item['chart']))
            except Exception as e:
                print("Osef + " + str(e))

            try:
                if item['button']:
                    containerNode.addChild(self.generateButtonNode(item['button']))
            except Exception as e:
                print("Osef + " + str(e))

            try:
                if item['form']:
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
        buttonNode = ButtonNode(data['buttonText'], data['destination'], data['name'], data['value'])

        return buttonNode

    def generateInput(self, data):
        print(data)
        inputNode = InputNode(data['type'], data['description'], data['value'], data['name'])
        return inputNode

    def generateChartNode(self, data):
        chartNode = ChartNode(data['name'], data['yAxe']['min'], data['yAxe']['max'])

        self.addJavascriptContent("generateChart(\"{}\", {}, {});".format(data['name'], data['yAxe']['min'], data['yAxe']['max']))
        return chartNode

    def generate(self, data):
        tree = Tree("html")

        if data['header']:
            tree.addChild(self.generateHeaderNode(data['header']))
        if data['body']:
            tree.addChild(self.generateBodyNode(data['body']))

        return tree



class Parser():
    def openConfigurationFile(self):
        with open("example.yaml", 'r') as stream:
            try:
                self.data = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def generateHtml(self):
        tree = TreeGenerator().generate(self.data)
        return generateTree(tree)

p = Parser()
p.openConfigurationFile()
