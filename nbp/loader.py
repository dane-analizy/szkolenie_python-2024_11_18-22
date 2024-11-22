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

from utils.config import load_config
from utils.db import disconnect_from_db, open_db
from sqlalchemy import text
from utils.nbp import get_nbp_data

# CONFIG_FILE = "db_config.yaml"
CONFIG_FILE = "db_config_lukasz.yaml"
LISTA_WALUT = ['EUR', 'USD', 'CHF', 'JPY']


config = load_config(CONFIG_FILE)
db_conn = open_db(config)

# tworzymy tabelkę
db_conn.execute(
    text("""
            create table if not exists waluty
            (
                data text,
                waluta text,
                kurs float
            );""")
)
db_conn.commit()

# pobranie danych z NBP
for m in range(1,12):
    for d in range(1,32):
        # pobieramy 1 dzień
        nbp_data = get_nbp_data(rok=2024, miesiac=m, dzien=d, obslugiwane_waluty=LISTA_WALUT)
        print(nbp_data)

        # jeśli nie było notowania - pomiń
        if LISTA_WALUT[0] not in nbp_data.keys():
            # print("pomijam")
            continue
        
        # notowanie było - włóż dane do bazy
        for waluta in LISTA_WALUT:
            zapytanie = f"""INSERT INTO
                            waluty (data, waluta, kurs)
                            VALUES (
                                '{nbp_data['data']}',
                                '{waluta.upper()}'
                                {nbp_data[waluta.upper()]}
                                )
                            """
            # print(zapytanie)
            db_conn.execute(text(zapytanie))
            db_conn.commit()

disconnect_from_db(db_conn)
