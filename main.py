import tkinter as tk
from tkinter import messagebox

# Sample product data
products = [
    {"name": "Cute Teddy Bear", "price": 10},
    {"name": "Pink Handbag", "price": 25},
    {"name": "Sweet Perfume", "price": 15},
    {"name": "Lovely Notebook", "price": 5},
    {"name": "Fluffy Pillow", "price": 20},
]

cart = []

# Function to add product to cart
def add_to_cart(product):
    cart.append(product)
    update_cart_display()

# Function to update cart display
def update_cart_display():
    cart_listbox.delete(0, tk.END)
    total_price = 0
    for item in cart:
        cart_listbox.insert(tk.END, f"{item['name']} - ${item['price']}")
        total_price += item["price"]
    
    total_label.config(text=f"Total: ${total_price}")

# Function to checkout
def checkout():
    if cart:
        messagebox.showinfo("Checkout", "Thank you for your purchase!")
        cart.clear()
        update_cart_display()
    else:
        messagebox.showwarning("Empty Cart", "Your cart is empty!")

# Create main window
root = tk.Tk()
root.title("Cute Shopping App")
root.geometry("400x500")
root.config(bg="#FFC0CB")  # Light pink background

# Product list section
product_frame = tk.Frame(root, bg="#FFC0CB")
product_frame.pack(pady=10)

tk.Label(product_frame, text="Products", font=("Arial", 14, "bold"), bg="#FFC0CB").pack()

for product in products:
    frame = tk.Frame(product_frame, bg="#FFC0CB")
    frame.pack(pady=5, padx=10, fill="x")
    
    tk.Label(frame, text=f"{product['name']} - ${product['price']}", bg="#FFC0CB").pack(side="left")
    tk.Button(frame, text="Add to Cart", command=lambda p=product: add_to_cart(p), bg="#FF69B4", fg="white").pack(side="right")

# Cart section
cart_label = tk.Label(root, text="Cart", font=("Arial", 14, "bold"), bg="#FFC0CB")
cart_label.pack(pady=5)

cart_listbox = tk.Listbox(root, width=40, height=6)
cart_listbox.pack(pady=5)

total_label = tk.Label(root, text="Total: $0", font=("Arial", 12), bg="#FFC0CB")
total_label.pack()

# Checkout button
checkout_button = tk.Button(root, text="Checkout", command=checkout, bg="#FF69B4", fg="white", font=("Arial", 12, "bold"))
checkout_button.pack(pady=10)

# Run the application
root.mainloop()
