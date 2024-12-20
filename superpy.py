import argparse
import csv
import sys
from datetime import datetime

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

# ! DIT WERKT NOG NIET HELEMAAL VANZELF - na 1e invoer moet ik rij aanpassen 
# De id-kolom wordt automatisch verhoogd voor elke nieuwe invoer in: bought.csv en sold.csv.
def get_next_id(filename):
    try: 
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            ids = [int(row[0]) for row in reader]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1

# AANKOPEN
def add_bought_product(product_name, buy_date, buy_price, expiration_date):
    next_id = get_next_id('bought.csv')
    with open('bought.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([next_id, product_name, buy_date, buy_price, expiration_date])
    print(f"Product {product_name} gekocht voor {buy_price} met vervaldatum {expiration_date}")

# VERKOPEN
# Elke invoer krijgt unieke id die wordt verhoogd voor elke nieuwe regel.
def add_sold_product(bought_id, sell_date, sell_price):
    next_id = get_next_id('sold.csv')
    with open('sold.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([next_id, bought_id, sell_date, sell_price])
    print(f"Product met id {bought_id} verkocht voor {sell_price}")

# INVENTARIS
def display_inventory():
    with open('bought.csv', mode='r') as file:
        reader = csv.reader(file)
        inventory = list(reader)
    print("Voorraad:")
    for item in inventory:
        print(item)

# TOTALE KOOPPRIJS PER PRODUCT
# toegevoegd voor versie 2
def display_total_buy_price_per_product():
    try:
        with open('bought.csv', mode='r') as file:
            reader = csv.DictReader(file)
            product_totals = {}
            for row in reader:
                print(f"Processing row: {row}")  # Debugging line
                product_name = row['product_name']
                buy_price = float(row['buy_price'])
                if product_name in product_totals:
                    product_totals[product_name] += buy_price
                else:
                    product_totals[product_name] = buy_price
        print("Totale koopprijs per product:")
        for product_name, total_buy_price in product_totals.items():
            print(f"{product_name}: {total_buy_price}")
    except FileNotFoundError:
        print("Error: 'bought.csv' file not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Superpy voorraadbeheersysteem")
    subparsers = parser.add_subparsers(dest="command")

    buy_parser = subparsers.add_parser('buy', help='Koop een product en voeg het toe aan de voorraad')
    buy_parser.add_argument('--product_name', required=True, help='Naam van het product dat je wilt kopen')
    buy_parser.add_argument('--buy_date', required=True, help='Aankoopdatum van het product in het formaat YYYY-MM-DD')
    buy_parser.add_argument('--buy_price', required=True, type=float, help='Koopprijs van het product')
    buy_parser.add_argument('--expiration_date', required=True, help='Vervaldatum van het product in het formaat YYYY-MM-DD')

    sell_parser = subparsers.add_parser('sell', help='Verkoop een product en verwijder het uit de voorraad')
    sell_parser.add_argument('--bought-id', required=True, type=int, help='ID-nr van het gekochte product')
    sell_parser.add_argument('--sell_date', required=True, help='Verkoopdatum van het product in het formaat YYYY-MM-DD')
    sell_parser.add_argument('--sell_price', required=True, type=float, help='Verkoopprijs van het product')

    inventory_parser = subparsers.add_parser('inventory', help='Bekijk de huidige voorraad')

    total_buy_price_parser = subparsers.add_parser('total_buy_price', help='Bekijk de totale aankoopprijs per product')

    args = parser.parse_args()

    print(f"Command: {args.command}")  # Debugging line

    if args.command == 'buy':
        add_bought_product(args.product_name, args.buy_date, args.buy_price, args.expiration_date)
    elif args.command == 'sell':
        add_sold_product(args.bought_id, args.sell_date, args.sell_price)
    elif args.command == 'inventory':
        display_inventory()
    elif args.command == 'total_buy_price':
        display_total_buy_price_per_product()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
