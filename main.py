class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = float(price)  # Ensure price is a float
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def getTotal(self):
        return self.price * self.qty

    def getDiscountedPrice(self):
        # Assuming some form of discount applies here
        return self.price * self.qty * 0.6

    def applyEnvironmentalFee(self):
        # Add environmental fee if the item is an electronic
        if self.category == "electronics":
            self.env_fee = 5 * self.qty
        return self.env_fee


# Class to handle shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.taxRate = 0.08
        self.memberDiscount = 0.05
        self.bigSpenderDiscount = 10
        self.couponDiscount = 0.15
        self.validCouponCode = "SAVE15"  # A valid coupon code
        self.currency = "USD"

    def addItem(self, item):
        # Add item to the cart
        self.items.append(item)

    def calculateSubtotal(self):
        # Calculate subtotal from all items in the cart
        subtotal = 0
        for item in self.items:
            subtotal += item.getTotal() + item.applyEnvironmentalFee()
        return subtotal

    def applyDiscounts(self, subtotal, isMember, hasCoupon):
        # Apply membership discount
        if isMember:
            subtotal -= subtotal * self.memberDiscount
        # Apply big spender discount if subtotal is greater than $100
        if subtotal > 100:
            subtotal -= self.bigSpenderDiscount
        return subtotal

    def calculateTotal(self, isMember, hasCoupon, couponCode):
        # Calculate total with tax and any discounts
        subtotal = self.calculateSubtotal()
        subtotal = self.applyDiscounts(subtotal, isMember, hasCoupon)

        # Add tax
        total = subtotal + (subtotal * self.taxRate)

        if hasCoupon and couponCode == self.validCouponCode:
            total -= total * self.couponDiscount

        return total


def main():
    # Create a new shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    item1 = Item("Apple", 1.5, 10)
    item2 = Item("Banana", 0.5, 5)
    item3 = Item("Laptop", 1000, 1)  # Corrected price to a number
    item3.category = "electronics"  # Mark it as an electronic item

    cart.addItem(item1)
    cart.addItem(item2)
    cart.addItem(item3)

    # Set whether user is a member and has a coupon
    isMember = True
    hasCoupon = True  # Changed to boolean for consistency
    couponCode = "SAVE15"  # Example coupon code

    # Calculate the total price
    total = cart.calculateTotal(isMember, hasCoupon, couponCode)

    # Print the total price or error message
    if total < 0:
        print("Error in calculation!")
    else:
        print(f"The total price is: ${total:.2f}")


if __name__ == "__main__":
    main()
