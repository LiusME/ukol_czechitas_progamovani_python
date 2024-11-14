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

    def __str__(self): 
        return (f"{self.estate_type.capitalize()} in locality {self.locality.name} " f"({self.locality.locality_coefficient}), {self.area} m², tax: {self.calculate_tax()} Kč.") 


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

    def __str__(self):
        commercial_status = "commercial" if self.commercial else "non-commercial"
        return (f"Residence in locality {self.locality.name} "
                f"({self.locality.locality_coefficient}), {self.area} m², "
                f"{commercial_status}, tax: {self.calculate_tax()} Kč.")
                
manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

zemedelsky_pozemek = Estate(manetin, 900, 'land')
print(zemedelsky_pozemek)

dum = Residence(manetin, 120, commercial=False)
print(dum)

kancelar = Residence(brno, 90, commercial=True)
print(kancelar)

