from math import ceil


class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality, area):        
        self.locality = locality
        self.area = area


class Estate(Property):
    def __init__(self, locality, area, estate_type):
        super().__init__(locality, area)
        self.estate_type = estate_type
        self.kind_of_coefficient = {
            "land": 0.85,
            "building site": 9,
            "forrest": 0.35,
            "garden": 2
        }

    def calculate_tax(self):
        estate_coefficient = self.kind_of_coefficient.get(self.estate_type, 0)
        calculation_estate = self.area *  estate_coefficient * self.locality.locality_coefficient
        return ceil(calculation_estate)

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality, area)
        self.commercial = commercial

    def calculate_tax(self):
        calculation_residence = self.area * self.locality.locality_coefficient * 15
        if self.commercial == True:
            return ceil(2 * calculation_residence)
        else:
            return ceil(calculation_residence)

manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

zemedelsky_pozemek = Estate(manetin, 900, 'land')



