#!/usr/bin/python3.9
import os
from sys import argv
from flask import Flask, request, render_template, send_file

workDir, ip, frontend_port, backend_port= argv
frontend_soket = ip + ":" + frontend_port
backend_soket = ip + ":" + backend_port

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
    query = request.args.get('query')
    
    if query == None: query = 0
    print(query)

    return render_template('dron.html')

@app.route('/<file>', methods=['GET'])
def start2(file):
    base = "/opt/waterDrone/src/modules/frontend/templates"

    if file:
        return send_file(f"{base}/{file}")
    return "Error"

@app.route('/<path>/<file>', methods=['GET'])
def start3(path, file):
    base = "/opt/waterDrone/src/modules/frontend/templates"
    abs_path = os.path.join(base, f"{path}/{file}")

    if file == "vue.global.js":
        return send_file(abs_path) 
    elif file:
        return send_file(abs_path)

    return "Error"

if __name__ == '__main__':
    app.run(host=ip, port=frontend_port)

