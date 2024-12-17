<<<<<<< HEAD
import argparse
import csv
import sys
from datetime import datetime

def add_bought_product(product_name, buy_price, expiration_date):
    with open('purchases.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_name, buy_price, expiration_date])
    print(f"Product {product_name} gekocht voor {buy_price} met vervaldatum {expiration_date}")

def add_sold_product(product_name, sell_price):
    with open('sales.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_name, sell_price])
    print(f"Product {product_name} verkocht voor {sell_price}")

def display_inventory():
    with open('purchases.csv', mode='r') as file:
        reader = csv.reader(file)
        inventory = list(reader)
    print("Voorraad:")
    for item in inventory:
        print(item)

def main():
    parser = argparse.ArgumentParser(description="Superpy voorraadbeheersysteem")
    subparsers = parser.add_subparsers(dest="command")

    buy_parser = subparsers.add_parser('buy', help='Koop een product en voeg het toe aan de voorraad')
    buy_parser.add_argument('--product-name', required=True, help='Naam van het product dat je wilt kopen')
    buy_parser.add_argument('--buy-price', required=True, type=float, help='Koopprijs van het product')
    buy_parser.add_argument('--expiration-date', required=True, help='Vervaldatum van het product in het formaat YYYY-MM-DD')

    sell_parser = subparsers.add_parser('sell', help='Verkoop een product en verwijder het uit de voorraad')
    sell_parser.add_argument('--product-name', required=True, help='Naam van het product dat je wilt verkopen')
    sell_parser.add_argument('--sell-price', required=True, type=float, help='Verkoopprijs van het product')

    inventory_parser = subparsers.add_parser('inventory', help='Bekijk de huidige voorraad')

    args = parser.parse_args()

    if args.command == 'buy':
        add_bought_product(args.product_name, args.buy_price, args.expiration_date)
    elif args.command == 'sell':
        add_sold_product(args.product_name, args.sell_price)
    elif args.command == 'inventory':
        display_inventory()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
=======
import argparse
import csv
import sys
from datetime import datetime

def add_bought_product(product_name, buy_price, expiration_date):
    with open('purchases.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_name, buy_price, expiration_date])
    print(f"Product {product_name} gekocht voor {buy_price} met vervaldatum {expiration_date}")

def add_sold_product(product_name, sell_price):
    with open('sales.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_name, sell_price])
    print(f"Product {product_name} verkocht voor {sell_price}")

def display_inventory():
    with open('purchases.csv', mode='r') as file:
        reader = csv.reader(file)
        inventory = list(reader)
    print("Voorraad:")
    for item in inventory:
        print(item)

def main():
    parser = argparse.ArgumentParser(description="Superpy voorraadbeheersysteem")
    subparsers = parser.add_subparsers(dest="command")

    buy_parser = subparsers.add_parser('buy', help='Koop een product en voeg het toe aan de voorraad')
    buy_parser.add_argument('--product-name', required=True, help='Naam van het product dat je wilt kopen')
    buy_parser.add_argument('--buy-price', required=True, type=float, help='Koopprijs van het product')
    buy_parser.add_argument('--expiration-date', required=True, help='Vervaldatum van het product in het formaat YYYY-MM-DD')

    sell_parser = subparsers.add_parser('sell', help='Verkoop een product en verwijder het uit de voorraad')
    sell_parser.add_argument('--product-name', required=True, help='Naam van het product dat je wilt verkopen')
    sell_parser.add_argument('--sell-price', required=True, type=float, help='Verkoopprijs van het product')

    inventory_parser = subparsers.add_parser('inventory', help='Bekijk de huidige voorraad')

    args = parser.parse_args()

    if args.command == 'buy':
        add_bought_product(args.product_name, args.buy_price, args.expiration_date)
    elif args.command == 'sell':
        add_sold_product(args.product_name, args.sell_price)
    elif args.command == 'inventory':
        display_inventory()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
>>>>>>> e3592188bed6a778bc450cbab54032c1a245a1fb
