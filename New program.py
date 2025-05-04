# Cake Management System

class Cake:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Quantity: {self.quantity})"

class CakeManagementSystem:
    def __init__(self):
        self.cakes = []

    def add_cake(self, name, price, quantity):
        self.cakes.append(Cake(name, price, quantity))
        print(f"Cake '{name}' added successfully!")

    def display_cakes(self):
        if not self.cakes:
            print("No cakes available.")
        else:
            print("Available Cakes:")
            for idx, cake in enumerate(self.cakes, start=1):
                print(f"{idx}. {cake}")

    def sell_cake(self, cake_index, quantity):
        if 0 <= cake_index < len(self.cakes):
            cake = self.cakes[cake_index]
            if cake.quantity >= quantity:
                cake.quantity -= quantity
                print(f"Sold {quantity} of '{cake.name}'.")
                if cake.quantity == 0:
                    self.cakes.pop(cake_index)
                    print(f"'{cake.name}' is now out of stock.")
            else:
                print(f"Not enough stock for '{cake.name}'. Available: {cake.quantity}")
        else:
            print("Invalid cake selection.")

def main():
    cms = CakeManagementSystem()

    while True:
        print("\nCake Management System")
        print("1. Add Cake")
        print("2. Display Cakes")
        print("3. Sell Cake")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter cake name: ")
            price = float(input("Enter cake price: "))
            quantity = int(input("Enter cake quantity: "))
            cms.add_cake(name, price, quantity)
        elif choice == "2":
            cms.display_cakes()
        elif choice == "3":
            cms.display_cakes()
            try:
                cake_index = int(input("Enter cake number to sell: ")) - 1
                quantity = int(input("Enter quantity to sell: "))
                cms.sell_cake(cake_index, quantity)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "4":
            print("Exiting Cake Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()