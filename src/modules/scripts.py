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
        self.run_script()


    def get_scripts(self):
        @self.backend.app.route('/get/scripts', methods=['GET'])
        def get_scripts():
            files = self._get_files()
            data = {}
            for file in files:
                data[file] = self._get_data(file)
            return json.dumps(data)

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

    def run_script(self):
        @self.backend.app.route('/run/script', methods=['POST'])
        def run_script():
            if request.method == 'POST':
                data = request.get_json()
                output = self._run_script(data['title'])
                return json.dumps(output)
                
            else: print("is not POST")
            return "False"

    # def get_script_data(self):
    #     @self.backend.app.route('/get/script/data', methods=['POST'])
    #     def get_script_data():
    #         if request.method == 'POST':
    #             data = request.get_json()
    #             title = data['title']

    #             text = self._get_data(title)
    #             return json.dumps(text)
    #         else: print("is not POST")

    #         return "OK"


    ########################################################################### 
    # Private methods    
    ###########################################################################     


    def _get_files(self):
        files = os.listdir(self.config.path)
        return files

    def _create_file(self, file, text):
        file = open(f"{self.config.path}/{file}.py", "w")
        file.writelines(text)
        file.close()

    def _get_data(self, file):
        path = self.config
        file = open(f"{self.config.path}/{file}", 'r')
        data = file.readlines()
        file.close()
        data = ''.join(data)
        return data

    def _run_script(self, file):
        output = os.popen(f"python3 {self.config.path}/{file}").read()
        return output