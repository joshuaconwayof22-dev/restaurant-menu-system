# Restaurant Menu System

A Python coursework project with a customer ordering window and a console-based menu management tool.

## Features

- Display menu items and prices from a CSV file.
- Add items to an order with a selected quantity.
- Calculate item subtotals and the order total.
- Clear or finish an order.
- View and add menu items using a separate console tool.

## Project Files

- `restaurant_app.py` — customer ordering interface built with guizero.
- `menu_editor.py` — console tool for viewing and adding menu items.
- `menu_full.csv` — shared menu data.
- `requirements.txt` — required Python packages.

## How to Run

Install Python 3, then open a terminal in the project folder.

Install the required package:

```bash
python -m pip install -r requirements.txt
```

Start the ordering application:

```bash
python restaurant_app.py
```

Or start the menu editor:

```bash
python menu_editor.py
```

Keep the CSV file in the same folder as both programs.
After saving changes in the menu editor, restart the ordering application to load the updated menu.

## Skills Practiced

Python functions, lists, dictionaries, CSV file handling, input validation, GUI development, and event handling.

## Limitations

This is a practice application. Orders are held in memory, and finishing an order displays a confirmation message. It does not process payments or save orders.