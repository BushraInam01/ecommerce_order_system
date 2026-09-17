# E-Commerce Order Processing System

A Python-based E-Commerce Order Processing System developed as part of a Python Intern Real-World Assessment.

The project processes customer orders, validates products and quantities, calculates discounts and shipping charges, handles payments, updates inventory, and generates a sales report.

## Project Overview

This project demonstrates practical Python programming concepts by building an order processing system without using classes, external libraries, databases, APIs, Django, FastAPI, or other frameworks.

The system is built using Python functions and core Python features.

## Features

- Order validation
- Product ID validation
- Quantity validation
- Stock availability checking
- Empty order handling
- Payment status validation
- Order subtotal calculation
- Discount calculation
- Shipping calculation
- Payment verification
- Revenue calculation
- Inventory updates
- Sales report generation
- Top customer identification
- Top-selling product identification
- Low-stock product detection
- Unique customer and category identification
- Configurable order processing using `**kwargs`
- Flexible calculations using `*args`
- Lambda functions for sorting
- List and set comprehensions
- LEGB scope demonstration
- Edge-case handling

## Business Rules

### Discounts

| Subtotal | Discount |
|----------|----------|
| $1000 or more | 15% |
| $500 - $999.99 | 10% |
| $200 - $499.99 | 5% |
| Below $200 | 0% |

### Shipping

| Subtotal | Shipping |
|----------|----------|
| $500 or more | Free |
| Below $500 | $20 |

### Payment

Only orders with a `paid` payment status are included in revenue and inventory updates.

### Inventory

Inventory is updated only when an order is valid and payment is completed.

## Product Data

The system contains the following products:

| Product ID | Product | Category | Price | Stock |
|------------|---------|----------|-------|-------|
| P001 | Laptop | Electronics | $1200 | 10 |
| P002 | Mouse | Accessories | $25 | 50 |
| P003 | Keyboard | Accessories | $75 | 20 |
| P004 | Monitor | Electronics | $300 | 15 |

## Sample Orders

The project includes multiple customer orders with different payment statuses.

- `ORD001` — Ali — Laptop + Mouse — Paid
- `ORD002` — Ahmed — Keyboard + Monitor — Paid
- `ORD003` — Ali — Mouse — Pending

The system processes each order according to the defined business rules.

## Python Concepts Used

This project demonstrates the following Python concepts:

### Functions

The system is divided into separate functions for different tasks, such as:

- `validate_order()`
- `calculate_subtotal()`
- `calculate_discount()`
- `calculate_shipping()`
- `is_payment_completed()`
- `calculate_revenue()`
- `update_inventory()`
- `generate_report()`
- `process_order()`

### `*args`

Used to allow a helper function to calculate totals from multiple amounts.

### `**kwargs`

Used in `process_order()` to provide configurable options such as:

- `apply_discount`
- `include_shipping`

Example:

```python
process_order(
    order,
    products,
    apply_discount=True,
    include_shipping=True
)
