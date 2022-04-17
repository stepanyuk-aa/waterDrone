class control():
    """
        Need 2 ESC
    """
    def __init__(self, ESC1, ESC2, backend):
        # Left
        self.ESC1 = ESC1
        # Rigrh
        self.ESC2 = ESC2
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

            return "OK"

    def to_stop(self):
        @self.backend.app.route('/to_stop', methods=['GET'])
        def to_stop():
            self.speed = 0
            self.ESC1.set_speed(self.speed)
            self.ESC2.set_speed(self.speed)
            return "OK"

    def to_direct(self):
        @self.backend.app.route('/to_direct', methods=['GET'])
        def to_direct():
            print(self.speed)
            self.ESC1.set_speed(self.speed)
            self.ESC2.set_speed(self.speed)
            return "OK"

    def to_left(self):
        @self.backend.app.route('/to_left', methods=['GET'])
        def to_left():
            self.ESC1.set_speed(self.speed / 2)
            self.ESC2.set_speed(self.speed)
            return "OK"

    def to_right(self):
        @self.backend.app.route('/to_right', methods=['GET'])
        def to_right():
            self.ESC1.set_speed(self.speed)
            self.ESC2.set_speed(self.speed / 2)
            return "OK"
    

