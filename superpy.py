import argparse
import csv
import sys
from datetime import datetime

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
# De id-kolom wordt automatisch verhoogd voor elke nieuwe invoer in: bought.csv en sold.csv.
# Elke invoer krijgt unieke id die wordt verhoogd voor elke nieuwe regel.

def add_sold_product(bought_id, sell_date, sell_price):
    next_id = get_next_id('sold.csv')
    with open('sold.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([next_id, bought_id, sell_date, sell_price])
    print(f"Product met id {bought_id} verkocht voor {sell_price}")

#INVENTARIS
def display_inventory():
    with open('bought.csv', mode='r') as file:
        reader = csv.reader(file)
        inventory = list(reader)
    print("Voorraad:")
    for item in inventory:
        print(item)

def main():
    parser = argparse.ArgumentParser(description="Superpy voorraadbeheersysteem")
    subparsers = parser.add_subparsers(dest="command")

    buy_parser = subparsers.add_parser('buy', help='Koop een product en voeg het toe aan de voorraad')
    buy_parser.add_argument('--product_name', required=True, help='Naam van het product dat je wilt kopen')
    buy_parser.add_argument('--buy_date', required=True, help='Aankoopdatum van het product in het formaat YYYY-MM-DD')
    buy_parser.add_argument('--buy_price', required=True, type=float, help='Koopprijs van het product')
    buy_parser.add_argument('--expiration_date', required=True, help='Vervaldatum van het product in het formaat YYYY-MM-DD')

    sell_parser = subparsers.add_parser('sell', help='Verkoop een product en verwijder het uit de voorraad')
    sell_parser.add_argument('--product-id', required=True, type=int, help='ID-nr van het product dat je wilt verkopen')
    sell_parser.add_argument('--bought-id', required=True, type=int, help='ID-nr van de verkoop')
    sell_parser.add_argument('--product-name', required=True, help='Naam van het product dat je wilt verkopen')
    sell_parser.add_argument('--sell-price', required=True, type=float, help='Verkoopprijs van het product')

    inventory_parser = subparsers.add_parser('inventory', help='Bekijk de huidige voorraad')

    args = parser.parse_args()

    if args.command == 'buy':
        add_bought_product(args.product_name, args.buy_date, args.buy_price, args.expiration_date)
    elif args.command == 'sell':
        add_sold_product(args.bought_id, args.sell_date, args.sell_price)
    elif args.command == 'inventory':
        display_inventory()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

