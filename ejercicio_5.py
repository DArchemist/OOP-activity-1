PI = 3.1416

class Circle:
    # First we initialize the variables

    radius = None

    # Then we create a constructor method to assign the radius to the Circle object

    def __init__(self, radius):
        self.radius = radius

    # Finally, we create methods to compute the area and the circumference of the circle

    def get_area(self) -> float:
        return PI * self.radius ** 2
    
    def get_circumference(self) -> float:
        return 2 * PI * self.radius
    

# To test the code, do

if __name__ == "__main__":
    circle = Circle(float(input('INGRESE EL RADIO DEL CÍRCULO: ')))
    print(f'EL ÁREA Y LA CIRCUNFERENCIA DEL CÍRCULO CON RADIO {circle.radius} SON {circle.get_area()}, Y {circle.get_circumference()} RESPECTIVAMENTE')