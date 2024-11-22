# pobieraczka danych z NBP i wkładająca dane do bazy

# create table if not exists waluty (
# 	data text,
# 	waluta text,
# 	kurs float
# );


# schemat działania
# 1. wczytanie konfiguracji
# 2. połączenie do bazy
# 3. utworzenie tabeli 'waluty' o ile nie istniała
# 4. dla każdego dnia i miesiąca - pobierz notowania z NBP przez API
# 5. te notowania zapisz do bazy
# 6. zamknij bazę danych
