# Import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox

# Import PIL for JPG image support
from PIL import Image, ImageTk


# Define the RestaurantOrderManagement class
class RestaurantOrderManagement:

    # Initialize the application
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Menu items and prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82  # USD → INR

        # Setup background
        self.setup_background()

        # Create main frame on canvas
        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window(400, 300, window=self.frame)

        # Heading
        ttk.Label(
            self.frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, pady=15)

        self.menu_labels = {}
        self.menu_quantities = {}

        # Menu items
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                self.frame,
                text=f"{item} ($ {price})",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            self.menu_labels[item] = label

            entry = ttk.Entry(self.frame, width=6)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = entry

        # Currency selection
        ttk.Label(
            self.frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(row=len(self.menu_items) + 1, column=0, pady=10)

        self.currency_var = tk.StringVar(value="USD")

        currency_dropdown = ttk.Combobox(
            self.frame,
            textvariable=self.currency_var,
            state="readonly",
            values=("USD", "INR"),
            width=10
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            pady=10
        )

        self.currency_var.trace("w", self.update_menu_prices)

        # Order button
        ttk.Button(
            self.frame,
            text="Place Order",
            command=self.place_order
        ).grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            pady=15
        )

    # Background setup
    def setup_background(self):
        self.canvas = tk.Canvas(self.root, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        image = Image.open("restaurant_management_bg.jpg")
        image = image.resize((800, 600))
        self.bg_image = ImageTk.PhotoImage(image)

        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

    # Update prices when currency changes
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price})")

    # Place order
    def place_order(self):
        total = 0
        summary = "Order Summary\n\n"

        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.menu_quantities.items():
            qty = entry.get()
            if qty.isdigit():
                qty = int(qty)
                if qty > 0:
                    price = self.menu_items[item] * rate
                    cost = qty * price
                    total += cost
                    summary += f"{item}: {qty} × {symbol}{price} = {symbol}{cost}\n"

        if total > 0:
            summary += f"\nTotal: {symbol}{total}"
            messagebox.showinfo("Order Placed", summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    RestaurantOrderManagement(root)
    root.mainloop()