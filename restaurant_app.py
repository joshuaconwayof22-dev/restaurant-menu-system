import csv
from guizero import App, Text, ListBox, TextBox, PushButton, Box

# load menu from csv
def load_menu_from_csv(filename):
#Reads menu_full.csv
    items = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append({
                "number": row["number"],
                "category": row["category"],
                "name": row["name"],
                "price": float(row["price"])
            })
    return items

#Format Menu Line
def format_menu_line(item):
    # Formats how each item will appear in the menu list.

    return f'{item["number"]}) {item["name"]} - ${item["price"]:.2f}'



#This list will store all ordered items (we'll fill it later)
order_items = []


def update_order_display():
#Shows each ordered item with quantity, unit price, subtotal,

    if not order_items:
        order_display.value = "No items ordered yet."
        return

    lines = []
    total = 0.0

    for item in order_items:
        qty = item["quantity"]
        name = item["name"]
        price = item["price"]
        subtotal = qty * price
        total += subtotal

        lines.append(f"{qty} x {name} @ ${price:.2f} = ${subtotal:.2f}")

    lines.append("-" * 35)
    lines.append(f"Grand Total: ${total:.2f}")

    order_display.value = "\n".join(lines)

# ----------------- BUTTON ACTIONS -----------------
def add_to_order():
#Add the selected menu item and quantity to the order_items list.

    # Get the selected text from the ListBox
    selected_text = menu_listbox.value

    #If nothing is selected, bail out
    if selected_text is None:
        order_display.value = "Select a menu item first."
        return

    #Find the index of that text in the ListBox items
    try:
        index = menu_listbox.items.index(selected_text)
    except ValueError:
        order_display.value = "Problem finding the selected item."
        return

    # Get menu item from list
    item = menu_items[index]

    # Quantity from the TextBox
    try:
        qty = int(quantity_box.value)
        if qty <= 0:
            raise ValueError
    except ValueError:
        order_display.value = "Enter a valid quantity (positive whole number)."
        return

    # Add to order list
    order_items.append({
        "number": item["number"],
        "category": item["category"],
        "name": item["name"],
        "price": item["price"],
        "quantity": qty
    })

    update_order_display()


def finish_order():
#Called when customer is done ordering.

    update_order_display()
    thank_you_text.value = "Thank you for your order!"


def clear_order():
#Clears the current order and resets the display.

    order_items.clear()
    order_display.value = "Order cleared."
    thank_you_text.value = ""

# ----------------- MAIN PROGRAM -----------------
# File name of the menu CSV
MENU_FILE = "menu_full.csv"

# Load items from CSV
menu_items = load_menu_from_csv(MENU_FILE)

# Create the main window
app = App("Los Pollos Hermanos", width=750, height=550, layout="grid")

# WELCOME TEXT
welcome = Text(app,
               text="Welcome to Los Pollos Hermanos!",
               grid=[0, 0, 3, 1],
               size=18,
               color="navy")

subtitle = Text(app,
                text="Please choose your items from the menu below:",
                grid=[0, 1, 3, 1],
                size=12)

# LEFT SIDE: MENU LIST
menu_label = Text(app, text="Menu Items", grid=[0, 2])

menu_listbox = ListBox(
    app,
    items=[format_menu_line(i) for i in menu_items],
    grid=[0, 3],
    width=200,
    height=400
)

# MIDDLE: QUANTITY + BUTTONS
middle = Box(app, layout="grid", grid=[1, 3])

qty_label = Text(middle, text="Quantity:", grid=[0, 0])
quantity_box = TextBox(middle, text="1", grid=[0, 1], width=5)

add_button = PushButton(middle, text="Add to Order",
                        command=add_to_order, grid=[0, 2])

finish_button = PushButton(middle, text="Finish Order",
                           command=finish_order, grid=[0, 3])

clear_button = PushButton(middle, text="Clear Order",
                          command=clear_order, grid=[0, 4])

# RIGHT SIDE: ORDER SUMMARY
order_label = Text(app, text="Your Order", grid=[2, 2])

order_display = Text(
    app,
    text="No items ordered yet.",
    grid=[2, 3],
    width=40,
    height=15
)

thank_you_text = Text(
    app,
    text="",
    grid=[0, 4, 3, 1],
    size=14,
    color="green"
)

# Start the GUI
app.display()
