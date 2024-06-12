class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity

    def remove_item(self, product_id, quantity):
        if product_id in self.items and self.items[product_id] >= quantity:
            self.items[product_id] -= quantity
            if self.items[product_id] == 0:
                del self.items[product_id]
        else:
            raise ValueError("Not enough items in inventory or item does not exist.")

    def check_item(self, product_id, quantity):
        return self.items.get(product_id, 0) >= quantity

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity

    def get_total_value(self):
        return sum(quantity for _, quantity in self.items.items())

class DiscountCoupon:
    def __init__(self, discount_percentage, max_discount_cap):
        self.discount_percentage = discount_percentage
        self.max_discount_cap = max_discount_cap

    def apply_discount(self, cart_value):
        discount = (cart_value * self.discount_percentage) / 100
        return min(discount, self.max_discount_cap)

class Store:
    def __init__(self):
        self.inventory = Inventory()
        self.carts = {}
        self.discount_coupons = {}

    def add_item_to_inventory(self, product_id, quantity):
        self.inventory.add_item(product_id, quantity)

    def remove_item_from_inventory(self, product_id, quantity):
        self.inventory.remove_item(product_id, quantity)

    def add_item_to_cart(self, customer_id, product_id, quantity):
        if self.inventory.check_item(product_id, quantity):
            if customer_id not in self.carts:
                self.carts[customer_id] = Cart()
            self.carts[customer_id].add_item(product_id, quantity)
            self.inventory.remove_item(product_id, quantity)
        else:
            raise ValueError("Item not available in inventory.")

    def apply_discount_coupon(self, customer_id, discount_id):
        if customer_id in self.carts and discount_id in self.discount_coupons:
            cart_value = self.carts[customer_id].get_total_value()
            discount = self.discount_coupons[discount_id].apply_discount(cart_value)
            return cart_value - discount
        else:
            raise ValueError("Invalid customer ID or discount ID.")

    def add_discount_coupon(self, discount_id, discount_percentage, max_discount_cap):
        self.discount_coupons[discount_id] = DiscountCoupon(discount_percentage, max_discount_cap)

def driver_function():
    store = Store()
    
    # Add items to inventory
    store.add_item_to_inventory("product1", 100)
    store.add_item_to_inventory("product2", 50)

    # Add discount coupons
    store.add_discount_coupon("DISCOUNT20", 20, 150)

    # Add items to cart
    try:
        store.add_item_to_cart("customer1", "product1", 10)
        store.add_item_to_cart("customer1", "product2", 5)
    except ValueError as e:
        print(e)

    # Apply discount coupon
    try:
        discounted_price = store.apply_discount_coupon("customer1", "DISCOUNT20")
        print(f"Discounted price: {discounted_price}")
    except ValueError as e:
        print(e)

    # Edge cases
    try:
        store.remove_item_from_inventory("product1", 200)
    except ValueError as e:
        print(e)

    try:
        store.add_item_to_cart("customer1", "product3", 5)
    except ValueError as e:
        print(e)

    try:
        discounted_price = store.apply_discount_coupon("customer1", "INVALID")
        print(f"Discounted price: {discounted_price}")
    except ValueError as e:
        print(e)

driver_function()
