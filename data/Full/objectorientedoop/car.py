class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"{self.model} is now driving.")


    def stop(self):
        print(f"{self.model} has stopped.")

    
    def honk(self):
        print(f"{self.model} is honking.")

    def describe(self):
        print(f"{self.model} is a {self.year} {self.color} car.")





       