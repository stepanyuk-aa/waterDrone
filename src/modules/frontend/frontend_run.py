#!/usr/bin/python3.9
from sys import argv
from flask import Flask, request, render_template

path, ip, frontend_port, backend_port= argv
frontend_soket = ip + ":" + frontend_port
backend_soket = ip + ":" + backend_port

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
    query = request.args.get('query')
    
    if query == None: query = 0
    print(query)

    return render_template('dron.html', speed=query, frontend=frontend_soket, backend=backend_soket)
 
if __name__ == '__main__':
    app.run(host=ip, port=frontend_port)

