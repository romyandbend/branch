class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\nItems in cart:")
            for item in self.items:
                print(f"{item.name} - ${item.price:.2f}")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"{name} removed from cart.")
                return
        print(f"{name} not found in cart.")

    def checkout(self):
        if not self.items:
            print("Cart is empty.")
        else:
            total = sum(item.price for item in self.items)
            print(f"\nTotal amount: ${total:.2f}")
            self.items.clear()
            print("Checkout complete.")
