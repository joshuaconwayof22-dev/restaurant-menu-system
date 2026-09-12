#!/usr/bin/env python3
import csv
from decimal import Decimal
from pathlib import Path

FILE = Path("menu_full.csv")
FIELDS = ["number", "category", "name", "price"]

def load_items():
    items = []
    if FILE.exists():
        with FILE.open("r", newline="", encoding="utf-8") as f:
            r = csv.DictReader(f)
            for row in r:
                try:
                    num = int(row.get("number", "").strip())
                    cat = (row.get("category") or "").strip()
                    name = (row.get("name") or "").strip()
                    price = Decimal((row.get("price") or "").strip())
                    if num > 0 and cat and name and price >= 0:
                        items.append({"number": num, "category": cat, "name": name, "price": f"{price:.2f}"})
                except Exception:
                    pass
    return items

def save_items(items):
    with FILE.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for it in sorted(items, key=lambda x: x["number"]):
            w.writerow(it)

def print_items(items):
    if not items:
        print("\n— No items yet —\n"); return
    print("\nCurrent Menu")
    print("----------------------------------------------")
    for it in items:
        print(f"{it['number']:>3}  {it['category']:<10} {it['name']:<24} ${it['price']}")
    print("----------------------------------------------\n")

def add_item(items):
    while True:
        try:
            num = int(input("Item number: ").strip())
            if num <= 0: raise ValueError()
            break
        except Exception:
            print("Enter a positive integer.")
    cat = input("Category (Drinks/Entrees/Sides): ").strip()
    while not cat:
        cat = input("Category cannot be blank: ").strip()
    name = input("Item name: ").strip()
    while not name:
        name = input("Name cannot be blank: ").strip()
    while True:
        try:
            price = Decimal(input("Price: ").strip())
            if price < 0: raise ValueError()
            break
        except Exception:
            print("Enter a non-negative number.")
    items.append({"number": num, "category": cat, "name": name, "price": f"{price:.2f}"})
    print("Added.\n")

def main():
    items = load_items()
    while True:
        print("1) View  2) Add  3) Save & Exit  4) Exit without saving")
        ch = input("Choose: ").strip()
        if ch == "1": print_items(items)
        elif ch == "2": add_item(items)
        elif ch == "3":
            save_items(items); print(f"Saved {len(items)} item(s) to {FILE.name}."); break
        elif ch == "4":
            print("Goodbye."); break
        else: print("Invalid choice.\n")

if __name__ == "__main__":
    main()
