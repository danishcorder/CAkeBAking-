# Define the base Car class
class Car:
    def __init__(self, model, color, engine_type):
        self.model = model
        self.color = color
        self.engine_type = engine_type

    def display_specs(self):
        print(f"Car Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Engine Type: {self.engine_type}")

# Car factory class
class CarFactory:
    def create_car(self, model, color, engine_type):
        print(f"Creating a {color} {model} with a {engine_type} engine...")
        return Car(model, color, engine_type)

# Example usage
def main():
    factory = CarFactory()

    # Create different car models
    car1 = factory.create_car("Sedan", "Red", "Petrol")
    car2 = factory.create_car("SUV", "Black", "Diesel")
    car3 = factory.create_car("Hatchback", "Blue", "Electric")

    # Display car specifications
    print("\nCar 1 Specifications:")
    car1.display_specs()

    print("\nCar 2 Specifications:")
    car2.display_specs()

    print("\nCar 3 Specifications:")
    car3.display_specs()

if __name__ == "__main__":
    main()