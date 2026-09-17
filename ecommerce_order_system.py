products = {
    "P001": {
        "name": "laptop",
        "price": 1200,
        "category": "Electronics",
        "stock": 10
    },
    "P002": {
        "name": "Mouse",
        "price": 25,
        "category": "Accessories",
        "stock": 50
    },
    "P003": {
        "name": "keyboard",
        "price": 75,
        "category": "Accessories",
        "stock": 20
    },
    "P004": {
        "name": "Monitor",
        "price": 300,
        "category": "Electronics",
        "stock": 15
    }
}


orders = [
    {
        "order_id": "ORD001",
        "customer": "Ali",
        "items": [
            {"product_id": "P001", "quantity": 1},
            {"product_id": "P002", "quantity": 2}
        ],
        "payment_status": "paid"
    },
    {
        "order_id": "ORD002",
        "customer": "Ahmed",
        "items": [
            {"product_id": "P003", "quantity": 2},
            {"product_id": "P004", "quantity": 1}
        ],
        "payment_status": "paid"
    },
    {
        "order_id": "ORD003",
        "customer": "Ali",
        "items": [
            {"product_id": "P002", "quantity": 5}
        ],
        "payment_status": "pending"
    }
]


# 1. Validate Orders

def validate_order(order, products):

    # Empty products dictionary
    if not products:
        return False, "Products dictionary is empty"

    # Order with no items
    if not order["items"]:
        return False, "Order has no items"

    # Invalid payment status
    if order["payment_status"] not in ["paid", "pending"]:
        return False, "Invalid payment status"

    for item in order["items"]:

        product_id = item["product_id"]
        quantity = item["quantity"]

        # Unknown product ID
        if product_id not in products:
            return False, "Unknown product id"

        # Zero or negative quantity
        if quantity <= 0:
            return False, "Quantity must be positive"

        # Quantity greater than stock
        if quantity > products[product_id]["stock"]:
            return False, "Insufficient Stock"

    return True, "Order is Valid"


# Test Validation

for order in orders:

    result = validate_order(order, products)

    print(order["order_id"], result)



# 2. Calculate Order Subtotal

def calculate_subtotal(order, products):

    subtotal = 0

    for item in order["items"]:

        product_id = item["product_id"]
        quantity = item["quantity"]

        price = products[product_id]["price"]

        item_total = price * quantity

        subtotal += item_total

    return subtotal


# Test Subtotal

for order in orders:

    subtotal = calculate_subtotal(order, products)

    print(
        order["order_id"],
        "Subtotal:",
        subtotal
    )



# 3. Apply Discounts

def calculate_discount(subtotal):

    if subtotal >= 1000:
        discount_rate = 0.15

    elif subtotal >= 500:
        discount_rate = 0.10

    elif subtotal >= 200:
        discount_rate = 0.05

    else:
        discount_rate = 0

    discount_amount = subtotal * discount_rate

    final_amount = subtotal - discount_amount

    return discount_amount, final_amount


# Test Discount

for order in orders:

    subtotal = calculate_subtotal(order, products)

    discount_amount, final_amount = calculate_discount(subtotal)

    print(
        order["order_id"],
        "Subtotal:", subtotal,
        "Discount:", discount_amount,
        "Final Amount:", final_amount
    )



# 4. Calculate Shipping

def calculate_shipping(subtotal):

    if subtotal >= 500:
        shipping = 0
    else:
        shipping = 20

    return shipping


# Test Shipping

subtotal = 600
shipping = calculate_shipping(subtotal)
print("Shipping:", shipping)

subtotal = 400
shipping = calculate_shipping(subtotal)
print("Shipping:", shipping)



# 5. Payment Handling

def is_payment_completed(order):

    if order["payment_status"] == "paid":
        return True
    else:
        return False


# Test Payment

for order in orders:

    if is_payment_completed(order):

        print(
            order["order_id"],
            "payment completed"
        )

    else:

        print(
            order["order_id"],
            "payment pending"
        )


# Calculate Revenue

def calculate_revenue(orders, products):

    revenue = 0

    for order in orders:

        is_valid, message = validate_order(
            order,
            products
        )

        if is_valid and is_payment_completed(order):

            subtotal = calculate_subtotal(
                order,
                products
            )

            discount_amount, final_amount = calculate_discount(
                subtotal
            )

            shipping = calculate_shipping(subtotal)

            total = final_amount + shipping

            revenue += total

    return revenue


# Test Revenue

revenue = calculate_revenue(
    orders,
    products
)

print("Total Revenue:", revenue)



# 6. Update Inventory

def update_inventory(order, products):

    for item in order["items"]:

        product_id = item["product_id"]
        quantity = item["quantity"]

        products[product_id]["stock"] -= quantity


# Process Orders

for order in orders:

    is_valid, message = validate_order(
        order,
        products
    )

    if is_valid and is_payment_completed(order):

        update_inventory(
            order,
            products
        )

        print(
            order["order_id"],
            "Inventory Updated"
        )

    else:

        print(
            order["order_id"],
            "Inventory Not Updated"
        )


# Check Inventory

print("\nUpdated Inventory:")

for product_id, product in products.items():

    print(
        product_id,
        product["name"],
        "Stock:",
        product["stock"]
    )



# 7. Generate Reports

def generate_report(orders, products):

    total_orders = len(orders)

    paid_orders = 0
    pending_orders = 0
    rejected_orders = 0

    total_revenue = 0
    total_discount = 0
    total_shipping = 0

    customer_orders = {}
    product_sales = {}

    for order in orders:

        is_valid, message = validate_order(
            order,
            products
        )

        if not is_valid:

            rejected_orders += 1
            continue

        if order["payment_status"] == "paid":

            paid_orders += 1

            subtotal = calculate_subtotal(
                order,
                products
            )

            discount_amount, final_amount = calculate_discount(
                subtotal
            )

            shipping = calculate_shipping(subtotal)

            total = final_amount + shipping

            total_revenue += total
            total_discount += discount_amount
            total_shipping += shipping

            # Customer Orders

            customer = order["customer"]

            if customer not in customer_orders:
                customer_orders[customer] = 0

            customer_orders[customer] += 1

            # Product Sales

            for item in order["items"]:

                product_id = item["product_id"]
                quantity = item["quantity"]

                if product_id not in product_sales:
                    product_sales[product_id] = 0

                product_sales[product_id] += quantity

        elif order["payment_status"] == "pending":

            pending_orders += 1


  
    # Top Customer

    if customer_orders:

        top_customer = max(
            customer_orders,
            key=customer_orders.get
        )

    else:

        top_customer = "No customer data"



    # Top-Selling Products with Tie Handling

    if product_sales:

        max_sales = max(
            product_sales.values()
        )

        top_products = [
            product_id
            for product_id, quantity in product_sales.items()
            if quantity == max_sales
        ]

    else:

        top_products = []



    # Low-Stock Products

    low_stock_products = [
        product_id
        for product_id, product in products.items()
        if product["stock"] <= 10
    ]



    # Unique Customers

    unique_customers = {
        order["customer"]
        for order in orders
    }



    # Unique Categories

    unique_categories = {
        product["category"]
        for product in products.values()
    }


    # Lambda Sorting

    sorted_customers = sorted(
        customer_orders.items(),
        key=lambda item: item[1],
        reverse=True
    )


    # Print Report

    print("\n===== SALES REPORT =====")

    print("Total Orders:", total_orders)
    print("Paid Orders:", paid_orders)
    print("Pending Orders:", pending_orders)
    print("Rejected Orders:", rejected_orders)

    print("Total Revenue:", total_revenue)
    print("Total Discount:", total_discount)
    print("Total Shipping Collected:", total_shipping)

    print("Top Customer:", top_customer)

    print("Top-Selling Products:", top_products)

    print("Low-Stock Products:", low_stock_products)

    print("Unique Customers:", unique_customers)

    print("Unique Categories:", unique_categories)

    print("Sorted Customer Orders:", sorted_customers)


generate_report(orders,products)


# ADVANCED REQUIREMENT 1
# Configurable Function using **kwargs

def process_order(order, products, **options):

    apply_discount = options.get(
        "apply_discount",
        True
    )

    include_shipping = options.get(
        "include_shipping",
        True
    )

    subtotal = calculate_subtotal(
        order,
        products
    )


    # Apply Discount

    if apply_discount:

        discount_amount, final_amount = calculate_discount(
            subtotal
        )

    else:

        discount_amount = 0
        final_amount = subtotal


    # Include Shipping

    if include_shipping:

        shipping = calculate_shipping(
            subtotal
        )

    else:

        shipping = 0


    total = final_amount + shipping

    return (
        subtotal,
        discount_amount,
        shipping,
        total
    )


# Test **kwargs

subtotal, discount, shipping, total = process_order(
    orders[0],
    products,
    apply_discount=True,
    include_shipping=True
)

print("\n===== PROCESS ORDER =====")

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Shipping:", shipping)
print("Total:", total)



# ADVANCED REQUIREMENT 2
# *args Meaningful Helper

def calculate_total(*amounts):

    total = 0

    for amount in amounts:

        total += amount

    return total


# Test *args

subtotal = 450
discount = 22.5
shipping = 20

final_total = calculate_total(
    subtotal,
    -discount,
    shipping
)

print("\n===== *ARGS TOTAL =====")

print("Final Total:", final_total)



# ADVANCED REQUIREMENT 3
# LEGB Demonstration

shipping_charge = 20


def calculate_example():

    discount = 10

    def final_amount():

        subtotal = 100

        return (
            subtotal
            - discount
            + shipping_charge
            + len("Paid")
        )

    return final_amount()


print("\n===== LEGB DEMO =====")

print(
    "LEGB Result:",
    calculate_example()
)

# L = Local
# E = Enclosing
# G = Global
# B = Built-in

