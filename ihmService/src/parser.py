#!/usr/bin/python
# coding: utf-8

import yaml
from .TreeGenerator import TreeGenerator

data = []

class Parser():
    def openConfigurationFile(self, fileNameConfig):
        fileNameConfig = "config/" + fileNameConfig + ".yaml"
        with open(fileNameConfig, 'r') as stream:
            try:
                self.data = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def generateHtml(self):
        tree = TreeGenerator().generate(self.data)
        return tree.generate()
