class car:
    def __init__(self,brand):
        self.brand=brand
        self.engine=self.Engine()
    class Engine:
        def start(self):
            print("Engine Started")
my_car=car("Marut")
my_car.engine.start()
