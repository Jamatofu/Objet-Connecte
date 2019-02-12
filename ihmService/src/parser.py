#!/usr/bin/python
# coding: utf-8

import yaml
from .TreeGenerator import TreeGenerator

data = []

class Parser():
    def openConfigurationFile(self):
        with open("example.yaml", 'r') as stream:
            try:
                self.data = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def generateHtml(self):
        tree = TreeGenerator().generate(self.data)
        return tree.generate()

p = Parser()
p.openConfigurationFile()
p.generateHtml()
