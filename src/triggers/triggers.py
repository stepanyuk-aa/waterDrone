import os
import subprocess


from drivers.ultrasonic import UltraSonic_driver
from drivers.GPS import GPS_driver


class triggers():
    def __init__(self, config):
        self.config = config.Triggers_config()
        self.path_service = f"{self.config.path_service}/{self.config.service_name}.service"
        self.path_link_service = f"{self.config.path_link}/{self.config.service_name}.service"

        self.path_timer = f"{self.config.path_service}/{self.config.service_name}.timer"
        self.path_link_timer = f"{self.config.path_link}/{self.config.service_name}.timer"

        try:
            if(self.check_service() == False):
                print(f"Status = {self.check_service() == False}")
                self.create_service()
                self.run_service()

            self.GPS = GPS_driver()
            self.Sonar = UltraSonic_driver()
        except:
            print("INIT ERROR")

    def check_service(self):
        print("CHECK")
        test = ""
        try:
            test = subprocess.check_output(f"systemctl status {self.config.service_name}.timer".split()).decode("utf-8")
        except:
            pass
        
        if "Active: active " in test:
            return True
        else:
            return False

    def create_service(self):
        print("CREATE")
        text_service = f"""[Unit]
Description=Triggers service for waterDrone
After=network.target
Wants=triggers.timer

[Service]
#User=root
Type=oneshot
WorkingDirectory=/opt/waterDrone/src/triggers
ExecStart=python3 /opt/waterDrone/src/triggers/triggers_run.py
#Restart=always

[Install]
WantedBy=multi-user.target"""

        text_timer = f"""[Unit]
Description=Triggers Timer
Requires=dron_triggers.service

[Timer]
Unit=dron_triggers.service
OnCalendar=*-*-* *:*:00/{self.config.interval}
AccuracySec=1ms

[Install]
WantedBy=timers.target"""

        file = open(self.path_service, 'w')
        file.writelines(text_service)
        file.close()

        file = open(self.path_timer, 'w')
        file.writelines(text_timer)
        file.close()

        try:
            os.unlink(f"{self.path_link_service}")
            os.unlink(f"{self.path_link_timer}")
            os.symlink(self.path_service, self.path_link_service)
            os.symlink(self.path_timer, self.path_link_timer)
        except:
            print("Error Create symlink")


    def run_service(self):
        print("RUN")
        subprocess.call("systemctl daemon-reload", shell = True)
        subprocess.call(f"systemctl restart {self.config.service_name}.timer", shell = True)
