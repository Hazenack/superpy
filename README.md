**SUPERPY**

Mijn Winc eindproject voor Python

Superpy is een voorraadbeheersysteem. Hiermee kan je producten kopen, verkopen, de voorraad bekijken en de totale aankoopprijs per product kan berekenen.

Ook kan de interne datum van het systeem gewijzigd worden.

**MANUAL**

Bestand opslaan en uitvoeren: Sla het bestand op.

Open een terminal in VS Code: 
Ga naar View > Terminal om een terminal te openen in VS Code.

Navigeer naar de projectdirectory:
Gebruik de cd-opdracht om naar de directory van je project te gaan.
Bijvoorbeeld:
cd path/to/your/project

Voer het script uit:
...

**VOORBEELD**

Voer het script uit vanuit de terminal met de volgende commando's:
`python superpy.py buy --product-name orange --buy-price 2.0 --expiration-date 2025-12-12`
`python superpy.py sell --product-name orange --sell-price 1.0`
`python superpy.py inventory`
`python superpy.py total_buy_price`
...

**COMMANDO'S**

1. **Koop een product en voeg het toe aan de voorraad:**
   $ python superpy.py buy --product_name <product_name> --buy_date <YYYY-MM-DD> --buy_price <price> --expiration_date <YYYY-MM-DD>

   Voorbeeld:
   $ python superpy.py buy --product_name appel --buy_date 2024-12-19 --buy_price 0.5 --expiration_date 2025-12-12

2. **Verkoop een product en verwijder het uit de voorraad:**
   $ python superpy.py sell --bought-id <id> --sell_date <YYYY-MM-DD> --sell_price <price>

   Voorbeeld:
   $ python superpy.py sell --bought-id 1 --sell_date 2024-12-20 --sell_price 0.75

3. **Bekijk de huidige voorraad:**
   $ python superpy.py inventory

   Voorbeeld:
   $ python superpy.py inventory

4. **Bekijk de totale aankoopprijs per product:**
   $ python superpy.py total_buy_price

   Voorbeeld:
   $ python superpy.py total_buy_price

5. **Verplaats de interne datum met een aantal dagen:**
   $ python superpy.py advance_time <days>

   Voorbeeld:
   $ python superpy.py advance_time 2

6. **Zet de interne datum terug naar vandaag:**
   $ python superpy.py advance_time 0

   Voorbeeld:
   $ python superpy.py advance_time 0
...

**BESTANDEN**
---------
1. **bought.csv**: Bevat de gekochte producten met de volgende kolommen:
   - id
   - product_name
   - buy_date
   - buy_price
   - expiration_date

2. **sold.csv**: Bevat de verkochte producten met de volgende kolommen:
   - id
   - bought_id
   - sell_date
   - sell_price

3. **current_date.txt**: Bevat de huidige interne datum van het systeem in het formaat YYYY-MM-DD.
...

**Foutopsporing**
. Krijg je een foutmelding krijgt over ontbrekende kolommen in een CSV-bestand? Controleer dan of de kolomkoppen correct zijn en overeenkomen met de verwachte kolommen.
. Als je een foutmelding krijgt over een ontbrekend bestand, zorg er dan voor dat het bestand bestaat en de juiste gegevens bevat.
...

