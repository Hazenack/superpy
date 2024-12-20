import argparse
import csv
import sys
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.

console = Console()

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
def add_sold_product(bought_id, sell_date, sell_price):
    next_id = get_next_id('sold.csv')
    with open('sold.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([next_id, bought_id, sell_date, sell_price])
    print(f"Product met id {bought_id} verkocht voor {sell_price}")

# INVENTARIS
def display_inventory():
    table = Table(title="Voorraad")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Product Name", style="magenta")
    table.add_column("Buy Date", justify="right", style="green")
    table.add_column("Buy Price", justify="right", style="green")
    table.add_column("Expiration Date", justify="right", style="green")

    with open('bought.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            table.add_row(*row)
    
    console.print(table)

# TOTALE KOOPPRIJS PER PRODUCT
# toegevoegd voor versie 2
def display_total_buy_price_per_product():
    try:
        with open('bought.csv', mode='r') as file:
            reader = csv.DictReader(file)
            product_totals = {}
            for row in reader:
                product_name = row['product_name']
                buy_price = float(row['buy_price'])
                if product_name in product_totals:
                    product_totals[product_name] += buy_price
                else:
                    product_totals[product_name] = buy_price
        
        table = Table(title="Totale koopprijs per product")
        table.add_column("Product Name", style="magenta")
        table.add_column("Total Buy Price", justify="right", style="green")

        for product_name, total_buy_price in product_totals.items():
            table.add_row(product_name, f"{total_buy_price:.2f}")
        
        console.print(table)
    except FileNotFoundError:
        console.print("[bold red]Error: 'bought.csv' file not found.[/bold red]")
    except KeyError as e:
        console.print(f"[bold red]Error: Missing expected column in CSV file: {e}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")

def get_current_date():
    try:
        with open('current_date.txt', mode='r') as file:
            return datetime.strptime(file.read().strip(), '%Y-%m-%d').date()
    except FileNotFoundError:
        current_date = datetime.now().date()
        with open('current_date.txt', mode='w') as file:
            file.write(current_date.strftime('%Y-%m-%d'))
        return current_date

def advance_time(days):
    current_date = get_current_date()
    new_date = current_date + timedelta(days=days)
    with open('current_date.txt', mode='w') as file:
        file.write(new_date.strftime('%Y-%m-%d'))
    print(f"Date advanced by {days} days. New date is {new_date}")

# omzet en winst [lastige puzzel maar werkt nu]
def calculate_revenue_and_profit(start_date, end_date):
    revenue = 0.0
    cost = 0.0

    try:
        with open('sold.csv', mode='r') as sold_file:
            sold_reader = csv.DictReader(sold_file)
            for row in sold_reader:
                sell_date = datetime.strptime(row['sell_date'], '%Y-%m-%d').date()
                if start_date <= sell_date <= end_date:
                    revenue += float(row['sell_price'])
                    bought_id = int(row['bought_id'])
                    cost += get_buy_price(bought_id)
        
        profit = revenue - cost
        console.print(f"[bold green]Revenue from {start_date} to {end_date}: {revenue:.2f}[/bold green]")
        console.print(f"[bold green]Profit from {start_date} to {end_date}: {profit:.2f}[/bold green]")
    except FileNotFoundError:
        console.print("[bold red]Error: 'sold.csv' file not found.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")

def get_buy_price(bought_id):
    try:
        with open('bought.csv', mode='r') as bought_file:
            bought_reader = csv.DictReader(bought_file)
            for row in bought_reader:
                if int(row['id']) == bought_id:
                    return float(row['buy_price'])
        return 0.0
    except FileNotFoundError:
        print("Error: 'bought.csv' file not found.")
        return 0.0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0.0

def export_bought_products(filename):
    try:
        with open('bought.csv', mode='r') as infile, open(filename, mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)
        print(f"Aangekochte product is geëxporteerd naar {filename}")
    except FileNotFoundError:
        print("Error: 'bought.csv' file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def export_sold_products(filename):
    try:
        with open('sold.csv', mode='r') as infile, open(filename, mode='w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                writer.writerow(row)
        print(f"Verkocht product is geëxporteerd naar {filename}")
    except FileNotFoundError:
        print("Error: 'sold.csv' file not found.")
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

    advance_time_parser = subparsers.add_parser('advance_time', help='Verplaats de interne datum met een aantal dagen')
    advance_time_parser.add_argument('days', type=int, help='Aantal dagen om de datum te verplaatsen')

    revenue_profit_parser = subparsers.add_parser('revenue_profit', help='Rapporteer omzet en winst over een bepaalde periode')
    revenue_profit_parser.add_argument('--start_date', required=True, help='Startdatum van de periode in het formaat YYYY-MM-DD')
    revenue_profit_parser.add_argument('--end_date', required=True, help='Einddatum van de periode in het formaat YYYY-MM-DD')

    export_bought_parser = subparsers.add_parser('export_bought', help='Exporteer gekochte producten naar een CSV-bestand')
    export_bought_parser.add_argument('filename', help='Naam van het CSV-bestand om naar te exporteren')

    export_sold_parser = subparsers.add_parser('export_sold', help='Exporteer verkochte producten naar een CSV-bestand')
    export_sold_parser.add_argument('filename', help='Naam van het CSV-bestand om naar te exporteren')

    args = parser.parse_args()

    print(f"Command: {args.command}")

    if args.command == 'buy':
        add_bought_product(args.product_name, args.buy_date, args.buy_price, args.expiration_date)
    elif args.command == 'sell':
        add_sold_product(args.bought_id, args.sell_date, args.sell_price)
    elif args.command == 'inventory':
        display_inventory()
    elif args.command == 'total_buy_price':
        display_total_buy_price_per_product()
    elif args.command == 'advance_time':
        advance_time(args.days)
    elif args.command == 'revenue_profit':
        start_date = datetime.strptime(args.start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(args.end_date, '%Y-%m-%d').date()
        calculate_revenue_and_profit(start_date, end_date)
    elif args.command == 'export_bought':
        export_bought_products(args.filename)
    elif args.command == 'export_sold':
        export_sold_products(args.filename)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
