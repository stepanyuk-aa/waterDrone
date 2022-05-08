import os
import subprocess


from drivers.ultrasonic import UltraSonic_driver
from drivers.GPS import GPS_driver


class triggers():
    def __init__(self, config):
        self.config = config.Triggers_config()
        self.path_service = f"{self.config.path_service}/{self.config.service_name}.service"
        self.path_link = f"{self.config.path_link}/{self.config.service_name}.service"

        #if(self.check_service()):
        #    self.run_service()
        #else:
            #self.create_service()
        #    self.run_service()

        self.GPS = GPS_driver()
        self.Sonar = UltraSonic_driver()

    def check_service(self):
        print("CHECK")
        test = ""
        try:
            test = subprocess.check_output(f"systemctl status {self.config.service_name}.service".split()).decode("utf-8")
        except:
            pass
        
        if "active (running)" in test:
            return True
        else:
            return False

    def create_service(self):
        print("CREATE")
        text = f"""[Unit]
Description=Triggers service for waterDrone
After=network.target

[Service]
User=root
WorkingDirectory=/opt/waterDrone/src/triggers
ExecStart=watch -n {self.config.interval} python3 /opt/waterDrone/src/triggers/triggers_run.py
Restart=always

[Install]
WantedBy=multi-user.target"""
        file = open(self.path_service, 'w')
        file.writelines(text)
        file.close()

        try:
            os.unlink(f"{self.config.path_link}/{self.config.service_name}.service")
            os.symlink(self.path_service, self.path_link)
        except:
            pass

    def run_service(self):
        print("RUN")
        subprocess.call("systemctl daemon-reload", shell = True)
        subprocess.call(f"systemctl restart {self.config.service_name}", shell = True)
