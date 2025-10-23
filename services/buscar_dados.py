from database.connect_db import abrir_cursor

def buscar_dados():
    # ! Ler o arquivo .sql
    with open("database/queries/veiculos_novos.sql", "r", encoding="utf-8") as f:
        sql_veiculos_novos = f.read()

    try:
        # * Abre a conexão com o banco de dados
        cursor, conn = abrir_cursor()

        # * Executa a query
        cursor.execute(sql_veiculos_novos)
        retorno = cursor.dict_fetchall()

        return retorno
    except Exception as e:
        print(f"Houve um erro na conexão com o banco de dados: {e}")
        return f"Houve um erro na conexão com o banco de dados: {e}"
    finally:
        cursor.close()
        conn.close()