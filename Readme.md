# Overview
This inventory management system allows administrators to manage inventory and customers to manage their shopping carts. It includes APIs to add and remove items from inventory, add items to the cart, and apply discount coupons. The system uses internal data structures without relying on external databases or services.

---
### APIs
- AddItemToInventory(productId, quantity): Adds the specified quantity of the item to the inventory.
- RemoveItemFromInventory(productId, quantity): Removes the specified quantity of the item from the inventory.
- AddItemToCart(customerId, productId, quantity): Adds the specified quantity of the item to the customer's cart if available in the inventory.
- ApplyDiscountCoupon(cartValue, discountId): Applies the discount coupon to the cart value and returns the discounted price.
---
### Edge Cases
Adding/removing more items than available in inventory.
Applying invalid discount coupons.
Adding items to the cart that are not available in the inventory.
