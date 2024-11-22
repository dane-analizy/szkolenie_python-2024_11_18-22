from sqlalchemy import create_engine, text


def make_connection_string(config):
    return f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"


def connect_to_db(conn_str):
    engine = create_engine(conn_str)
    conn = engine.connect()
    return conn


def disconnect_from_db(conn):
    conn.close()


def open_db(config):
    con_str = make_connection_string(config)
    return connect_to_db(con_str)


def run_db_query(conn, sql_query):
    return conn.execute(text(sql_query))
