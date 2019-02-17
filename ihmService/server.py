#!/usr/bin/python
# coding: utf-8

from flask import Flask, request, render_template,Response
from flask_cors import CORS
from flask import jsonify
from src.parser import Parser

app = Flask(__name__)
CORS(app)

dataChart = {}
dataButtonDict = {}

def addDataChart(name, data):
    chart = []

    if name in dataChart:
        chart = dataChart[name]
    else:
        dataChart[name] = chart

    if(len(chart) >= 15):
        chart.pop()

    dataChart[name].append(data)

@app.route("/<site>", methods=['POST', 'GET'])
def addConfigurationFile(site):
    if request.method == 'POST':
        fileName = "config/" + site + ".yaml"
        with open(fileName, "w") as f:
            f.write(request.form['content'])
    elif request.method == 'GET':
        parser = Parser()
        parser.openConfigurationFile(site)
        return parser.generateHtml()

    return "200"


@app.route("/chart/<sensor>", methods=['POST', 'GET'])
def getDataChart(sensor):
    if request.method == 'GET':
        if sensor in dataChart :
            result = ""
            dataList = dataChart.get(sensor)
            if len(dataList) > 0:
                result = dataList.pop()
                
            return jsonify(result)
        else:
            return jsonify("")
    elif request.method == 'POST':
        addDataChart(sensor, request.get_json())
        return 'Cool'

@app.route("/button/<name>", methods=['POST', 'GET'])
def dataButton(name):
    print(name)
    if request.method == 'GET':
        if name in dataButtonDict :
            print("Ca y est")
            result = dataButtonDict.get(name)

            return jsonify(result)
        return jsonify(False)
    elif request.method == 'POST':
        dataButtonDict[name] = request.form['value']
        print("Bien ajoute")
        return "200"
