import os
from config import Frontend_config
from modules.frontend.panelsTemplate import *

class frontend():
    def __init__(self):
        self.config = Frontend_config()
        self.path_service = f"{self.config.path_service}/{self.config.service_name}.service"
        self.path_link = f"{self.config.path_link}/{self.config.service_name}.service"
        self.backend_soket = f"{self.config.ip}:{self.config.backend_port}"
    def run(self):    
        self.create_service()

        try:
            self.create_link()
            self.create_conrol_panel()
            self.create_scripts_panel()
        except:
            print("Fronted start ERROR")
            pass
        
        os.system("systemctl daemon-reload")

    def create_service(self):
        text = f"""[Unit]
Description=Frontend service for waterDrone
After=network.target

[Service]
User=root
WorkingDirectory={self.config.working_directory}
ExecStart={self.config.working_directory}/frontend_run.py {self.config.ip} {self.config.port} {self.config.backend_port}
Restart=always

[Install]
WantedBy=multi-user.target"""

        
        file = open(self.path_service, 'w')
        file.writelines(text)
        file.close()

    def create_link(self):
        if os.path.isfile(f"{self.config.path_link}/{self.config.service_name}.service"):
            os.unlink(f"{self.config.path_link}/{self.config.service_name}.service")
        
        os.symlink(self.path_service, self.path_link)

    def create_conrol_panel():
        path = "/opt/waterDrone/src/modules/frontend/templates/components/control.js"
        os.remove(path)
        file = open(path, 'w')
        file.writelines(gen_control_panel(self.backend_soket))
        file.close()

    def create_scripts_panel():
        path = "/opt/waterDrone/src/modules/frontend/templates/components/scripts.js"
        os.remove(path)
        file = open(path, 'w')
        file.writelines(gen_control_panel(self.backend_soket))
        file.close()

    def start_service(self):
        # self.logger.info("modules > frontend > start_service")
        os.system("systemctl restart dron_frontend")

    def stop_service(self):
        os.system("systemctl stop dron_frontend")
