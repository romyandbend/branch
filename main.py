from cart import Cart
from item import Item

def display_menu():
    print("\n1. Add item to cart")
    print("2. View cart")
    print("3. Remove item from cart")
    print("4. Checkout")
    print("5. Exit")

def main():
    cart = Cart()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            item = Item(name, price)
            cart.add_item(item)
        elif choice == '2':
            cart.view_cart()
        elif choice == '3':
            name = input("Enter item name to remove: ")
            cart.remove_item(name)
        elif choice == '4':
            cart.checkout()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
