class Number:
    # First we initialize the variables

    value = None

    # Then we create a constructor method to encapsulate the value

    def __init__(self, value):
        self.value = value

    # Finally, we create methods to compute the square and the cube of the number

    def get_square(self) -> float:
        return self.value ** 2
    
    def get_cube(self) -> float:
        return self.value ** 3
    

# To test the code, do

if __name__ == "__main__":
    number = Number(float(input('INGRESE UN NÚMERO PARA CALCULAR SU CUADRADO Y SU CUBO: ')))
    print(f'EL CUADRADO DE {number.value} ES: {number.get_square()}, Y SU CUBO ES: {number.get_cube()}')