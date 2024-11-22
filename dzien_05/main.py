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
