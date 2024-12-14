class Order:
    def __init__(self, order_number, items):
        self.order_number = order_number
        self.items = items

class OrderTotalCalculator:
    @staticmethod
    def calculate_total(order):
        
        total = sum(order.items)
        return total

class OrderPrinter:
    @staticmethod
    def print_order_details(order):
        print(f"Order Number: {order.order_number}")

order1 = Order(2000, [20, 10.5, 5.5])

total = OrderTotalCalculator.calculate_total(order1)

print(f"Total: {total}")

OrderPrinter.print_order_details(order1)