#!/opt/waterDrone/venv/bin/python
from sys import argv
from flask import Flask, request, render_template

path, ip, port = argv
soket = ip + ":" + port

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
    query = request.args.get('query')
    
    if query == None: query = 0
    print(query)

    return render_template('dron.html', speed=query, ip=soket)
 
if __name__ == '__main__':
    app.run(host=ip, port=port)

