# database_manager.py

import psycopg2
from configparser import ConfigParser

class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        # Lee los datos de conexión desde el archivo secret.config
        config = ConfigParser()
        config.read(r'C:\Users\santy\Downloads\E5\app\models\secret.cfg')

        self.host = config.get('database', 'PGHOST')
        self.database = config.get('database', 'PGDATABASE')
        self.user = config.get('database', 'PGUSER')
        self.password = config.get('database', 'PGPASSWORD')

        # Establece la conexión a la base de datos
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def execute_query(self, query):
        # Ejecuta una consulta en la base de datos
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def execute_query_with_params(self, query, params):
        # Ejecuta una consulta con parámetros en la base de datos
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result

    def execute_insert_query(self, query, params):
        # Ejecuta una consulta de inserción en la base de datos
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()


"""
class PensionModel:
    def __init__(self):
        # Connection to the database using configuration values
        self.conn = psycopg2.connect(
            host=SecretConfig.PGHOST,
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            port=SecretConfig.PGPORT
        )
        self.cursor = self.conn.cursor()

    def create_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS pension (
                id SERIAL PRIMARY KEY,
                edad_actual INTEGER NOT NULL,
                sexo VARCHAR(10) NOT NULL,
                salario_actual FLOAT NOT NULL,
                semanas_laboradas INTEGER NOT NULL,
                ahorro_actual FLOAT NOT NULL,
                rentabilidad_fondo FLOAT NOT NULL,
                tasa_administracion FLOAT NOT NULL
            );
        '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_pension(self, pension_data):
        insert_query = '''
            INSERT INTO pension (edad_actual, sexo, salario_actual, semanas_laboradas, ahorro_actual, rentabilidad_fondo, tasa_administracion)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        '''
        self.cursor.execute(insert_query, pension_data)
        self.conn.commit()

    def update_pension(self, pension_id, pension_data):
        update_query = '''
            UPDATE pension
            SET edad_actual=%s, sexo=%s, salario_actual=%s, semanas_laboradas=%s, ahorro_actual=%s, rentabilidad_fondo=%s, tasa_administracion=%s
            WHERE id=%s;
        '''
        data_to_update = pension_data + (pension_id,)
        self.cursor.execute(update_query, data_to_update)
        self.conn.commit()

    def delete_pension(self, pension_id):
        delete_query = '''
            DELETE FROM pension
            WHERE id=%s;
        '''
        self.cursor.execute(delete_query, (pension_id,))
        self.conn.commit()

    def get_pension(self, pension_id):
        select_query = '''
            SELECT * FROM pension
            WHERE id=%s;
        '''
        self.cursor.execute(select_query, (pension_id,))
        return self.cursor.fetchone()
    
    def query_by_age(self, current_age):
        select_query = '''
            SELECT * FROM pension
            WHERE edad_actual=%s;
        '''
        self.cursor.execute(select_query, (current_age,))
        return self.cursor.fetchall()

    def query_by_gender(self, gender):
        select_query = '''
            SELECT * FROM pension
            WHERE sexo=%s;
        '''
        self.cursor.execute(select_query, (gender,))
        return self.cursor.fetchall()

    def query_by_salary(self, current_salary):
        select_query = '''
            SELECT * FROM pension
            WHERE salario_actual=%s;
        '''
        self.cursor.execute(select_query, (current_salary,))
        return self.cursor.fetchall()

    def query_by_weeks_worked(self, weeks_worked):
        select_query = '''
            SELECT * FROM pension
            WHERE semanas_laboradas=%s;
        '''
        self.cursor.execute(select_query, (weeks_worked,))
        return self.cursor.fetchall()

    def query_by_current_savings(self, current_savings):
        select_query = '''
            SELECT * FROM pension
            WHERE ahorro_actual=%s;
        '''
        self.cursor.execute(select_query, (current_savings,))
        return self.cursor.fetchall()

    def query_by_fund_profitability(self, fund_profitability):
        select_query = '''
            SELECT * FROM pension
            WHERE rentabilidad_fondo=%s;
        '''
        self.cursor.execute(select_query, (fund_profitability,))
        return self.cursor.fetchall()

    def query_by_administration_fee_rate(self, administration_fee_rate):
        select_query = '''
            SELECT * FROM pension
            WHERE tasa_administracion=%s;
        '''
        self.cursor.execute(select_query, (administration_fee_rate,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def check_record_existence(self, table, record_data):
        select_query = f"SELECT * FROM {table} WHERE id=%s;"  # Assuming the first value of record_data is the ID
        self.cursor.execute(select_query, (record_data[0],))  # Assuming the ID is in the first position
        return self.cursor.fetchone() is not None
"""