class car:

    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color

    def drive(self):
        print(self.model+ "Car is driving")
    

    def stop(self):
        print(self.model +"Car is stopped")
    

