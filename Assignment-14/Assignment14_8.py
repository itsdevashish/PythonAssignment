class vehicle:
    def start(self):
        print("vehicle is starting...")

class car(vehicle):
    def start(self):
        super().start()  
        print("car is starting.")


v = vehicle()
v.start()

c = car()
c.start()
