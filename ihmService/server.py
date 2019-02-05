#!/usr/bin/python
# coding: utf-8

from flask import Flask, request, render_template,Response
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

# sensor / List(Of data)
dataChart = {}

def addDataChart(name, data):
    chart = []

    if name in dataChart:
        chart = dataChart[name]
    else:
        dataChart[name] = chart

    if(len(chart) >= 15):
        chart.pop()

    dataChart[name].append(data)


@app.route("/user",  methods=['POST', 'GET'])
def home():
    with open("result.txt", "w") as f:
        f.write("lol")
    if request.method == 'POST':
        return "thx"
    return "GET"

@app.route("/chart/<sensor>", methods=['POST', 'GET'])
def getDataChart(sensor):
    if request.method == 'GET':
        # return jsonify(
        #     x=datetime.datetime.now(),
        #     y=23
        # )

        if sensor in dataChart :
            result = ""
            dataList = dataChart.get(sensor)
            if len(dataList) > 0:
                result = dataList.pop()
            print(result)

            print("Nb d'element => " + str(result))
            return jsonify(result)
        else:
            return jsonify("")
    elif request.method == 'POST':
        addDataChart(sensor, request.get_json())
        return 'Cool'

@app.route("/<id>", methods=['POST'])
def addConfiguration(id):
    fileName = "config/" + id + ".yaml"
    with open(fileName, "w") as f:
        f.write(str(request.data))
    return "200"