class ZestyZomato:
    def __init__(self):
        self.menu = []
        self.orders = []
        self.order_id = 1

    def add_dish(self, dish_id, dish_name, price):
        dish = {
            'dish_id': dish_id,
            'dish_name': dish_name,
            'price': price,
            'availability': True
        }
        self.menu.append(dish)
        print(f"New dish '{dish_name}' added to the menu.")

    def remove_dish(self, dish_id):
        for dish in self.menu:
            if dish['dish_id'] == dish_id:
                self.menu.remove(dish)
                print(f"Dish with ID '{dish_id}' removed from the menu.")
                return
        print(f"Dish with ID '{dish_id}' not found in the menu.")

    def update_dish_availability(self, dish_id, availability):
        for dish in self.menu:
            if dish['dish_id'] == dish_id:
                dish['availability'] = availability
                print(f"Availability of dish with ID '{dish_id}' updated to {availability}.")
                return
        print(f"Dish with ID '{dish_id}' not found in the menu.")

    def take_order(self, customer_name, dish_ids):
        order_dishes = []
        for dish_id in dish_ids:
            dish = next((dish for dish in self.menu if dish['dish_id'] == dish_id), None)
            if dish:
                if dish['availability']:
                    order_dishes.append(dish)
                else:
                    print(f"Dish with ID '{dish_id}' is not available.")
            else:
                print(f"Dish with ID '{dish_id}' not found in the menu.")
        if order_dishes:
            order = {
                'order_id': self.order_id,
                'customer_name': customer_name,
                'dishes': order_dishes,
                'status': 'received'
            }
            self.orders.append(order)
            self.order_id += 1
            print(f"Order with ID {order['order_id']} placed successfully.")

    def update_order_status(self, order_id, status):
        for order in self.orders:
            if order['order_id'] == order_id:
                order['status'] = status
                print(f"Order with ID {order_id} status updated to '{status}'.")
                return
        print(f"Order with ID {order_id} not found.")

    def review_orders(self):
        if self.orders:
            for order in self.orders:
                print(f"Order ID: {order['order_id']}, Customer: {order['customer_name']}, Status: {order['status']}")
        else:
            print("No orders found.")

    def show_menu(self):
        if self.menu:
            print("Menu:")
            for dish in self.menu:
                availability = "Available" if dish['availability'] else "Not available"
                print(f"ID: {dish['dish_id']}, Name: {dish['dish_name']}, Price: {dish['price']}, {availability}")
        else:
            print("Menu is empty.")

    def run(self):
        print("Welcome to Zesty Zomato!")
        while True:
            print("\nSelect an option:")
            print("1. Add a dish to the menu")
            print("2. Remove a dish from the menu")
            print("3. Update dish availability")
            print("4. Take a new order")
            print("5. Update order status")
            print("6. Review all orders")
            print("7. Show menu")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                dish_id = input("Enter dish ID: ")
                dish_name = input("Enter dish name: ")
                price = float(input("Enter dish price: "))
                self.add_dish(dish_id, dish_name, price)
            elif choice == "2":
                dish_id = input("Enter dish ID to remove: ")
                self.remove_dish(dish_id)
            elif choice == "3":
                dish_id = input("Enter dish ID to update availability: ")
                availability = input("Enter availability (True/False): ").lower() == "true"
                self.update_dish_availability(dish_id, availability)
            elif choice == "4":
                customer_name = input("Enter customer name: ")
                dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
                self.take_order(customer_name, dish_ids)
            elif choice == "5":
                order_id = int(input("Enter order ID to update status: "))
                status = input("Enter new status: ")
                self.update_order_status(order_id, status)
            elif choice == "6":
                self.review_orders()
            elif choice == "7":
                self.show_menu()
            elif choice == "8":
                print("Thank you for using Zesty Zomato. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")


# Usage example
zesty_zomato = ZestyZomato()
zesty_zomato.run()
