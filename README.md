**SUPERPY**

Mijn Winc eindproject voor Python.

Superpy is een voorraadbeheersysteem. Hiermee kan je producten kopen, verkopen, de voorraad bekijken en de totale aankoopprijs per product berekenen.
---------

**MANUAL**

Bestand opslaan en uitvoeren: Sla het bestand op.

Open een terminal in VS Code: 
Ga naar View > Terminal om een terminal te openen in VS Code.

Navigeer naar de projectdirectory:
Gebruik de cd-opdracht om naar de directory van je project te gaan.
Bijvoorbeeld:
cd path/to/your/project

Voer het script uit.

**VOORBEELD**

Voer het script uit vanuit de terminal met de volgende commando's:
`python superpy.py buy --product-name orange --buy-price 2.0 --expiration-date 2025-12-12`
`python superpy.py sell --product-name orange --sell-price 1.0`
`python superpy.py inventory`
`python superpy.py total_buy_price`
---------

**COMMANDO'S**

## Product Kopen
Voeg een product toe aan de voorraad:
```bash
python superpy.py buy --product_name "Appel" --buy_date "2023-10-01" --buy_price 0.50 --expiration_date "2023-10-10"
```

### Product Verkopen
Verkoop een product uit de voorraad:
```bash
python superpy.py sell --bought-id 1 --sell_date "2023-10-05" --sell_price 0.75
```

### Voorraad Weergeven
Bekijk de huidige voorraad:
```bash
python superpy.py inventory
```

### Totale Aankoopprijs per Product
Bekijk de totale aankoopprijs per product:
```bash
python superpy.py total_buy_price
```

### Datum Verplaatsen
Verplaats de interne datum met een aantal dagen:
```bash
python superpy.py advance_time 5
```

### Omzet en Winst Berekenen
Rapporteer omzet en winst over een bepaalde periode:
```bash
python superpy.py revenue_profit --start_date "2023-10-01" --end_date "2023-10-10"
```

### Gekochte Producten Exporteren
Exporteer gekochte producten naar een CSV-bestand:
```bash
python superpy.py export_bought export_bought.csv
```

### Verkochte Producten Exporteren
Exporteer verkochte producten naar een CSV-bestand:
```bash
python superpy.py export_sold export_sold.csv
```

### Statistieken Visualiseren
Visualiseer statistieken met Matplotlib:
```bash
python superpy.py visualize
```
---------

**Foutopsporing**

1. Krijg je foutmelding over ontbrekende kolommen in een CSV-bestand? Controleer of de kolomkoppen correct zijn en overeenkomen met de verwachte kolommen.
2. Bij een foutmelding over een ontbrekend bestand: zorg er dan voor dat het bestand bestaat en de juiste gegevens bevat.
---------

**RAPPORT**

**Inleiding**

Dit rapport bespreekt drie belangrijke punten van dit `superpy` script. Deze zijn de automatische aanmaak van ID's voor CSV-bestanden, het gebruik van `rich` voor het weergeven van tabellen, en de integratie van Matplotlib voor het visualiseren van statistieken.

**Automatische ID aanmaak**

De functie `get_next_id` maakt automatisch unieke ID's aan voor nieuwe invoer in de bestanden `bought.csv` en `sold.csv`. Deze functie leest de bestaande ID's uit het CSV-bestand, bepaalt de hoogste ID en verhoogt deze met één voor de nieuwe invoer. Elke unieke ID invoer is belangrijk is voor het bijhouden van producten. 

**Rich voor Tabellen**

`rich` wordt gebruikt om tabellen in de console weer te geven. Functies zoals `display_inventory` en `display_total_buy_price_per_product` gebruikende `Table` class uit `rich` om tabellen te maken. Dit geeft leesbare gegevens.

** Matplotlib**
Met Matplotlib in de functie `visualize_statistics` kunnen staafdiagrammen gemaakt worden die de aankoopprijzen van producten laten zien. Deze functie leest gegevens uit het `bought.csv` bestand, haalt productnamen en aankoopprijzen op en maakt een staafdiagram. Dit geeft een visuele gegevens weergave waarmee trends en patronen ontdekt kunnen worden.

**Conclusie**

De implementatie van automatische ID-generatie, het gebruik van de `rich` bibliotheek voor het weergeven van tabellen, en de integratie van Matplotlib voor het visualiseren van statistieken zijn drie belangrijke technische elementen van het `superpy` script. Elk element lost specifieke problemen op en verbetert de functionaliteit en gebruikerservaring van het script. Deze functies maken het script betrouwbaarder, gebruiksvriendelijker en visueel aantrekkelijker, wat bijdraagt aan een betere algehele ervaring voor de gebruiker.

**EIND**
---------