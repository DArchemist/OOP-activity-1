class FamilyAges:
    # First we initialize the variables

    juans_age = None
    albertos_age = None
    anas_age = None
    moms_age = None

    # Then we define a public method to compute the ages 

    def compute_ages(self) -> object:
        self.juans_age = float(input('INGRESE LA EDAD DE JUAN: '))
        self.albertos_age = 2 / 3 * self.juans_age
        self.anas_age = 4 / 3 * self.juans_age
        self.moms_age = self.juans_age + self.albertos_age + self.anas_age
        return self # Returning the object allows for method chaining

    # Finally, we define a public method for printing the ages

    def print_ages(self) -> None:
        print(f'LAS EDADES SON: ALBERTO: {self.albertos_age:.0f} JUAN: {self.juans_age:.0f} ANA: {self.anas_age:.0f} MAMÁ: {self.moms_age:.0f}')
        

# To test the code, do

if __name__ == '__main__':
    FamilyAges().compute_ages().print_ages()