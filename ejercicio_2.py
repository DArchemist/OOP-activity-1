class Sum:
    # First we initialize the variables

    suma = None
    x = None
    y = None

    # Then we define a public method to compute the sum

    def compute_sum(self) -> object:
        self.suma = 0
        self.x = 20
        self.suma = self.suma + self.x
        self.y = 40
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y
        return self

    # Finally, we define a public method for printing the sum

    def print_sum(self) -> None:
        print(f'EL VALOR DE LA SUMA ES: {self.suma}')


# To test the code, do

if __name__ == '__main__':
    Sum().compute_sum().print_sum()