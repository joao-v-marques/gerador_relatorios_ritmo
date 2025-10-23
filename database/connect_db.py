import oracledb, os, logging, json
logging.basicConfig(level=logging.INFO)

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'configs.json')

with open(config_path, "r", encoding="utf-8") as file:
    config = json.load(file)

def conexaoOrcl():
    login = config['banco']['user']
    senha = config['banco']['pass']
    dsn =  config['banco']['dns']
    
    oracledb.init_oracle_client(lib_dir=config['banco']['instant_client'])

    try:
        connection = oracledb.connect(user=login, password=senha, dsn=dsn)
        logging.info("Conexão com Oracle estabelecida com sucesso.")
        return connection
    
    except oracledb.DatabaseError as e:
        error, = e.args
        logging.error(f"Erro ao conectar ao os dados do json: {error}")

def abrir_cursor():
    conn = conexaoOrcl()
    if not conn:
        logging.error('Deu merda no conexaoOrcl')
        raise ConnectionError('Não foi possível conectar ao Oracle.')
    cursor = conn.cursor()

    def dict_fetchall(cursor):
        colunas = [desc[0].lower() for desc in cursor.description]
        return [dict(zip(colunas, row)) for row in cursor.fetchall()]
    
    def dict_fetchone(cursor):
        colunas = [desc[0].lower() for desc in cursor.description]
        row = cursor.fetchone()
        return dict(zip(colunas, row)) if row else None
    
    cursor.dict_fetchall = lambda: dict_fetchall(cursor)
    cursor.dict_fetchone = lambda: dict_fetchone(cursor)
    return cursor, conn


