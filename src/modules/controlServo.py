class control():
    """
        Need Servo and ESC
    """
    def __init__(self, ESC, Servo, backend):
        self.ESC = ESC
        self.Servo = Servo

        self.backend = backend
        self.speed = 0

        self.set_speed()
        self.to_stop()
        self.to_direct()
        self.to_left()
        self.to_right()

    def set_speed(self):
        @self.backend.app.route('/set_speed/<speed>', methods=['GET'])
        def set_speed(speed):
            if speed == None: 
                self.speed = 0
            else:
                self.speed = speed

            print(f"Set speed to {self.speed}")
            self.ESC.set_speed(self.speed)
            return "OK"

    def to_stop(self):
        @self.backend.app.route('/to_stop', methods=['GET'])
        def to_stop():
            self.speed = 0
            self.ESC.set_speed(self.speed)
            return "OK"

    def to_direct(self):
        @self.backend.app.route('/to_direct', methods=['GET'])
        def to_direct():
            print("Servo Rount to direct")
            self.Servo.set_direct()
            return "OK"

    def to_left(self):
        @self.backend.app.route('/to_left', methods=['GET'])
        def to_left():
            print("Servo Rount to left")
            self.Servo.set_left()
            return "OK"

    def to_right(self):
        @self.backend.app.route('/to_right', methods=['GET'])
        def to_right():
            print("Servo Rount to right")
            self.Servo.set_right()
            return "OK"
    

