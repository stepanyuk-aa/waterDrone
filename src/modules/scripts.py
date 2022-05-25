import os
import json
from flask import request

class scripts():
    def __init__(self, config, backend):
        self.config = config
        self.backend = backend

        self.get_scripts()
        self.create_script()
        self.delite_script()
        self.get_script_data()


    def get_scripts(self):
        @self.backend.app.route('/get/scripts', methods=['GET'])
        def get_scripts():
            return self._get_files()

    def create_script(self):
        @self.backend.app.route('/create/script', methods=['POST'])
        def create_script():
            if request.method == 'POST':
                data = request.get_json()
                title = data['title']
                text = data['text']

                self._create_file(title, text)
            else: print("is not POST")
            return "OK"

    def delite_script(self):
        @self.backend.app.route('/delite/script', methods=['POST'])
        def delite_script():
            if request.method == 'POST':
                data = request.get_json()
                title = data['title']

                os.remove(f"{self.config.path}/{title}.py")
            else: print("is not POST")

            return "OK"

    def get_script_data(self):
        @self.backend.app.route('/get/script/data', methods=['POST'])
        def get_script_data():
            if request.method == 'POST':
                data = request.get_json()
                title = data['title']

                text = self._get_data(title)
                return json.dumps(text)
            else: print("is not POST")

            return "OK"


    ########################################################################### 
    # Private methods    
    ###########################################################################     


    def _get_files(self):
        files = os.listdir(self.config.path)
        return json.dumps(files)

    def _create_file(self, title, text):
        file = open(f"{self.config.path}/{title}.py", "w")
        file.writelines(text)
        file.close()

    def _get_data(self, title):
        path = self.config
        file = open(f"{self.config.path}/{title}.py", 'r')
        data = file.readlines()
        file.close()

        return data
    