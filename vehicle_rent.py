from datetime import date

class Vehicle:
    def __init__(self, brand, model, year, price_per_day):
        self.specs = (brand, model, year) 
        self.price_per_day = price_per_day
        self.available = True

    def calculate_rent(self, days):
        return self.price_per_day * days

    def __str__(self):
        return f"{self.specs[0]} {self.specs[1]} ({self.specs[2]}) - {self.price_per_day}€/day"

class Car(Vehicle): 
    def calculate_rent(self, days): 
        base = super().calculate_rent(days)
        return base * 1.2 

class Bike(Vehicle):
    def calculate_rent(self, days):
        base = super().calculate_rent(days)
        return base * 0.7 

class Fleet:
    def __init__(self):
        self.vehicles = [] 
        self.rented_ids = set()

    def add_vehicles(self, *vehicles): 
        self.vehicles.extend(vehicles)

    @staticmethod
    def discount(days): 
        return 0.9 if days > 7 else 1.0

    @classmethod
    def from_specs(cls, specs_list): 
        fleet = cls()
        for brand, model, year, price, type_ in specs_list:
            if type_ == "car":
                fleet.add_vehicles(Car(brand, model, year, price))
            else:
                fleet.add_vehicles(Bike(brand, model, year, price))
        return fleet

    def rent(self, **kwargs): 
        brand = kwargs.get('brand')
        for v in self.vehicles:
            if v.specs[0] == brand and v.available:
                v.available = False
                self.rented_ids.add(v.specs) 
                return v
        return None

if __name__ == "__main__":
    specs = [
        ("Skoda", "Octavia", 2020, 30, "car"),
        ("VW", "Golf", 2022, 35, "car"),
        ("Kellys", "MTB", 2023, 10, "bike"),
    ]

    fleet = Fleet.from_specs(specs)

    print(f"Fleet: {len(fleet.vehicles)} vehicles")
    for v in fleet.vehicles:
        print(f" - {v}")

    # rent Skoda for 5 days
    car = fleet.rent(brand="Skoda")
    days = 5
    price = car.calculate_rent(days) * Fleet.discount(days)
    print(f"\nRented: {car} for {days} days = {price}€")

    # try rent same brand again 
    car2 = fleet.rent(brand="Skoda")
    print(f"Second rent Skoda: {car2}") # None = not available
    print(f"Rented IDs (set): {fleet.rented_ids}")

    # rent bike for 10 days with discount
    bike = fleet.rent(brand="Kellys")
    days = 10
    price = bike.calculate_rent(days) * Fleet.discount(days)
    print(f"\nRented: {bike} for {days} days with discount = {price}€")