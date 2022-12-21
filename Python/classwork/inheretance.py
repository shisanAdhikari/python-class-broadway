
class vehicle:
    def __init__(self, color , year,n_seats,n_tyres,engine_types ):
        self.color = color
        self.year = year
        self.n_seats = n_seats
        self.n_tyres = n_tyres
        self.engine_types = engine_types

    def print_info(self):

        print(f"The color of vehicle is : {self.color}")


class Motorcycle(vehicle):
    def __init__(self,color,year,n_seats,n_tyres,engine_types):
        super().__init__(color, year)
        self.num_tyres = n_tyres
        self.num_seats = n_seats

    def start_engine(self):
      print("starting......vroom")



class ElectricMotorcycle(Motorcycle):
    def __init__(self,color,year,n_seats,n_tyres,engine_types):
        self.engine_types = engine_types







v = vehicle("Black",2018)
v.print_info()

m = Motorcycle("Black",2018,2,2,"Petrol")
m.start_engine()

e = ElectricMotorcycle("White",2020,2,2,"Electric")







