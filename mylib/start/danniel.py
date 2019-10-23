class Ball:
    def __init__(self,type):
        self.type = type
        self.run()

    def run(self):
        print("You are kicking the ball")

    def hello(self):
        print("Hello")

def standalone():
    print("Run the method separately")
