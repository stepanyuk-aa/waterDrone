from config import Backend_config
# from sys import argv
from flask import Flask, request, render_template


class backend():
    def __init__(self):    
        self.app = Flask(__name__)
        self.config = Backend_config()
        self.start()

    def start(self):
        @self.app.route('/', methods=['GET'])
        def start():
            query = request.args.get('query')
            
            if query == None: query = 0
            print(query)
            return "OK"
 
    def run(self):
        self.app.run(host=self.config.ip, port=self.config.port)


# b = backend()
# b.run()