# https://dbeaver.io/download/

# Tworzymy tabelę w bazie:

# create table players (
# 	player_id serial primary key,
# 	first_name text not null,
# 	last_name text not null,
# 	height numeric not null,
# 	weight numeric not null
# );


# Wkładamy do niej trochę danych:

# insert into players (first_name,last_name,height,weight)
# values ('Jan', 'Kowalski', 184, 85);

# insert into players (first_name,last_name,height,weight)
# values ('Marian', 'Nowak', 190, 50);

# insert into players (first_name,last_name,height,weight)
# values ('Zdzisław', 'Dyrman', 173 ,74);

# insert into players (first_name,last_name,height,weight)
# values ('Zenon', 'Brzęczyk', 164, 95);

# insert into players (first_name,last_name,height,weight)
# values ('Chuck','Norris', 182, 78);

# insert into players (first_name,last_name,height,weight)
# values ('Krzysztof','Jarzyna', 168, 70);


# potrzebne pakiety: SQLAlchemy - framework
# pakiet do konkretnego typu bazy: https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls
# - pakiet do łączenia się z PostgreSQL
# 		- `pip install psycopg2`
# 	- pakiet do łączenia się z Oracle
# 		- `pip install cx_oracle`
# 	- pakiet do łączenia się z MS SQL
# 		- `pip install pymssql`


# connection string - adres do bazy danych
# conn_str = "postgresql+psycopg2://<UserName>:<Password>@<Database_Host>/<Database_Name>

# w utils/config.py - utworzona funkcja do czytania konfiguracji

# from utils.config import load_config
# from sqlalchemy import create_engine, text

# # CONFIG_FILE = "db_config.yaml"
# CONFIG_FILE = "db_config_lukasz.yaml"

# config = load_config(CONFIG_FILE)

# conn_str = f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
# # print(conn_str)

# engine = create_engine(conn_str)
# print(engine)

# conn = engine.connect()
# print(conn)

# results = conn.execute(text("SELECT * FROM players;"))
# print(results)

# for record in results:
#     print(record)

# conn.close()


#### ZADANIE 34

# Napisz funkcję, która przyjmie przez parametr nazwę pliku do którego zapisze wszystkie
# wiersze z tabeli `players` (w bazie) w formacie csv

# plan:
# 1. wczytać konfigurację
# 2. połączyć się do bazy danych
# 3. pobrać dane z bazy -> zapytanie: "SELECT * FROM players;"
# 4. wyniki zapisać do pliku (otworzyć plik, sformatować wyniki do postaci rekord = 1 linia, zapisać kolejne linie)
# 5. posprzątać: zamknąć bazę, zamknąć plik


# from utils.config import load_config
# from utils.db import disconnect_from_db, open_db, run_db_query

# # CONFIG_FILE = "db_config.yaml"
# CONFIG_FILE = "db_config_lukasz.yaml"


# def db_to_csv(config, nazwa_pliku):
#     # 1. wczytać konfigurację
#     config = load_config(config)

#     # 2. połączyć się do bazy danych
#     db_conn = open_db(config)

#     # 3. pobrać dane z bazy -> zapytanie: "SELECT * FROM players;"
#     query = """
#     SELECT
#         first_name
#         , weight
#         , last_name
#     FROM
#         players
#     WHERE
#         weight < 80
#     ;
#     """

#     res = run_db_query(db_conn, query)

#     # 4. wyniki zapisać do pliku (otworzyć plik, sformatować wyniki do postaci rekord = 1 linia, zapisać kolejne linie)
#     with open(nazwa_pliku, "w", encoding="utf-8") as plik:
#         for linia in res:
#             # print(linia)
#             # linia_zapis = (
#             #     str(linia[0])
#             #     + ";"
#             #     + linia[1]
#             #     + ";"
#             #     + linia[2]
#             #     + ";"
#             #     + str(linia[3])
#             #     + ";"
#             #     + str(linia[4])
#             # )
#             linia_zapis = ";".join([str(el) for el in linia])
#             # print(linia_zapis)
#             plik.write(linia_zapis + "\n")

#     disconnect_from_db(db_conn)
#     # 5. posprzątać: zamknąć bazę, zamknąć plik


# db_to_csv(CONFIG_FILE, "zawodnicy.csv")


# przechodzenie przez dwie listy na raz
l1 = [1, 2, 3, 4]
l2 = ["a", "b", "c", "d", "e"]

# for indeks, el1 in enumerate(l1):
#     print(el1, l2[indeks])

# for indeks, el2 in enumerate(l2):
#     print(el2, l1[indeks])

# for el2, el1 in zip(l2, l1):
#     print(el1, el2)


# from utils.config import load_config
# from utils.db import disconnect_from_db, open_db, run_db_query
# import json

# # CONFIG_FILE = "db_config.yaml"
# CONFIG_FILE = "db_config_lukasz.yaml"

# config = load_config(CONFIG_FILE)
# db_conn = open_db(config)

# query = "SELECT * FROM players;"
# res = run_db_query(db_conn, query)

# # nazwy kolumn z wyników
# cols = list(res.keys())


# # lista słowników
# wyniki = []
# for record in res:
#     print("="*40)

#     record_dict = {}
#     for el, column_name in zip(record, cols):
#         # print(f"{column_name} => {el}")
#         if not isinstance(el, (str, int, float)):
#             el = str(el)
#         record_dict[column_name] = el

#     print(record_dict)
#     wyniki.append(record_dict)

# disconnect_from_db(db_conn)

# with open("dane.json", "w", encoding="utf-8") as f:
#     json.dump(wyniki, f)


# zapis danych do bazy

# INSERT INTO teableka (kolumna, kolumn2, kolumn3) VALUES (1,2,3)

# from utils.config import load_config
# from utils.db import disconnect_from_db, open_db
# from sqlalchemy import text

# # CONFIG_FILE = "db_config.yaml"
# CONFIG_FILE = "db_config_lukasz.yaml"

# config = load_config(CONFIG_FILE)
# db_conn = open_db(config)

# rekordy = [
#     {
#         "imie": "Druga Halina",
#         "nazwisko": "Kowalska-Bąk",
#         "wzrost": 1.65,
#         "waga": 59,
#     },
#     {"imie": "Druga Krystyna", "nazwisko": "Góral", "wzrost": 1.71, "waga": 58},
#     {"imie": "Druga Zosia", "nazwisko": "Iksińska", "wzrost": 1.84, "waga": 65}
# ]

# for osoba in rekordy:
#     imie = osoba["imie"]
#     nazwisko = osoba["nazwisko"]
#     wzrost = osoba["wzrost"]
#     waga = osoba["waga"]

#     zapytanie = f"""
#     INSERT INTO players (first_name, last_name, height, weight)
#     VALUES ('{imie}', '{nazwisko}', {wzrost}, {waga})
#     """

#     print(zapytanie)
#     db_conn.execute(text(zapytanie))
#     db_conn.commit() # to jest koniecznie przy zapisywaniu zmian do bazy

# disconnect_from_db(db_conn)


# nieco inaczej

# from utils.config import load_config
# from utils.db import disconnect_from_db, open_db
# from sqlalchemy import text

# # CONFIG_FILE = "db_config.yaml"
# CONFIG_FILE = "db_config_lukasz.yaml"

# config = load_config(CONFIG_FILE)
# db_conn = open_db(config)

rekordy = [
    {
        "imie": "Trzecia Halina",
        "nazwisko": "Kowalska-Bąk",
        "wzrost": 1.65,
        "waga": 59,
    },
    {"imie": "Trzecia Krystyna", "nazwisko": "Góral", "wzrost": 1.71, "waga": 58},
    {"imie": "Trzecia Zosia", "nazwisko": "Iksińska", "wzrost": 1.84, "waga": 65},
]

# for osoba in rekordy:
#     zapytanie = """
#     INSERT INTO players (first_name, last_name, height, weight)
#     VALUES (:imie, :nazwisko, :wzrost, :waga)
#     """
#     print(osoba)
#     print(zapytanie)
#     db_conn.execute(text(zapytanie), osoba )
#     db_conn.commit()  # to jest koniecznie przy zapisywaniu zmian do bazy

# disconnect_from_db(db_conn)


# osoba = rekordy[0]
# print(osoba)
# lista_kolumny = ", ".join(osoba.keys())
# print(lista_kolumny)
# lista_kluczy = ", ".join( [f":{k}" for k in osoba.keys()])
# print(lista_kluczy)
# zapytanie = "INSERT INTO players (" + lista_kolumny + ") VALUES (" + lista_kluczy + ");"

# print(zapytanie)

# db_conn.excute(text(zapytanie), osoba)


# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
