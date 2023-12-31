#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import sqlite3 # importa a biblioteca de banco de dados

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Database(): # classe para o banco de dados
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def __init__(self):

        pass

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def open_conn(self): # método para conectar ao banco de dados

        self.conn = sqlite3.connect('DB000') # objeto de conexao com o banco de dados de nome clientes
        self.cursor = self.conn.cursor()     # objeto de cursor para executar comando SQL

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def close_conn(self): # método para desconectar o banco de dados

        self.conn.close() # objeto de encerramento de conexao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def create_table(self): # método de manipulacao e criacao de tabelas

        self.open_conn() # chama o método de conexao com o banco de dados

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tab_admins (
                            username CHAR(40) PRIMARY KEY,
                            password TEXT
                            );
                            """)
        
        self.conn.commit() # insere o comando SQL

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tab_employees (
                            ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                            IDC TEXT,
                            name TEXT, 
                            age INTEGER,
                            sex TEXT,
                            address TEXT,
                            phone INTEGER,
                            marital_status TEXT,
                            dependents INTEGER,
                            nationality TEXT,
                            city TEXT,
                            job_position TEXT,
                            salary DECIMAL (5,2),
                            work_shift TEXT
                            );
                            """)
        
        self.conn.commit() # insere o comando SQL

        self.close_conn()  # chama o método para encerrar a conexao

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def insert_into(self): # método para inserir dados nas tabelas

        self.open_conn() # chama o método de conexao com o banco de dados

        admin_list = [        # lista de admins
            ('user1', '123'),
            ('user2', '132'),
            ('user3', '321')
        ]

        insert_query = "INSERT INTO tab_admins (username, password) VALUES (?, ?)" # string de query

        for user_data in admin_list:                     # ciclo para iterar sobre os elementos da lista
            self.cursor.execute(insert_query, user_data) # executa a query na tupla

        self.conn.commit() # insere o comando SQL
        self.close_conn()   

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def fill_employees(self):

        self.open_conn()

        employees_list = [
            ('IDC1', 'John Doe', 30, 'Male', '123 Main St', 5551234, 'Single', 0, 'American', 'New York', 'Manager', 5000.00, 'Day'),
            ('IDC2', 'Jane Smith', 25, 'Female', '456 Oak St', 5555678, 'Married', 2, 'Canadian', 'Toronto', 'Developer', 4000.00, 'Night'),
            ('IDC3', 'Bob Johnson', 40, 'Male', '789 Pine St', 5559012, 'Divorced', 1, 'British', 'London', 'Analyst', 3500.00, 'Day'),
            ('IDC4', 'Alice Brown', 28, 'Female', '101 Cedar St', 5553456, 'Single', 0, 'Australian', 'Sydney', 'Designer', 4500.00, 'Night'),
            ('IDC5', 'Mike Miller', 35, 'Male', '202 Elm St', 5557890, 'Married', 3, 'German', 'Berlin', 'Engineer', 6000.00, 'Day'),
            ('IDC6', 'Sara Davis', 32, 'Female', '303 Birch St', 5552345, 'Single', 0, 'French', 'Paris', 'Manager', 5500.00, 'Night'),
            ('IDC7', 'Tom Wilson', 45, 'Male', '404 Maple St', 5556789, 'Married', 2, 'Spanish', 'Madrid', 'Developer', 4200.00, 'Day'),
            ('IDC8', 'Emily White', 27, 'Female', '505 Walnut St', 5550123, 'Single', 0, 'Italian', 'Rome', 'Analyst', 3700.00, 'Night'),
            ('IDC9', 'Jack Taylor', 38, 'Male', '606 Pine St', 5554567, 'Married', 1, 'Chinese', 'Beijing', 'Designer', 4800.00, 'Day'),
            ('IDC10', 'Sophie Clark', 29, 'Female', '707 Oak St', 5558901, 'Divorced', 0, 'Japanese', 'Tokyo', 'Engineer', 6200.00, 'Night'),
            ('IDC11', 'Chris Lee', 33, 'Male', '808 Cedar St', 5552345, 'Single', 0, 'Korean', 'Seoul', 'Manager', 5800.00, 'Day'),
            ('IDC12', 'Emma Johnson', 31, 'Female', '909 Elm St', 5556789, 'Married', 2, 'Russian', 'Moscow', 'Developer', 4300.00, 'Night'),
            ('IDC13', 'Mark Brown', 42, 'Male', '111 Birch St', 5550123, 'Divorced', 1, 'Indian', 'Mumbai', 'Analyst', 3600.00, 'Day'),
            ('IDC14', 'Laura Miller', 26, 'Female', '222 Maple St', 5554567, 'Single', 0, 'Brazilian', 'Rio de Janeiro', 'Designer', 4900.00, 'Night'),
            ('IDC15', 'Daniel Davis', 34, 'Male', '333 Walnut St', 5558901, 'Married', 3, 'Mexican', 'Mexico City', 'Engineer', 6100.00, 'Day')
        ]
    
        insert_query = "INSERT INTO tab_employees (IDC, name, age, sex, address, phone, marital_status, dependents, nationality, city, job_position, salary, work_shift) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

        for user_data in employees_list:
            self.cursor.execute(insert_query, user_data)

        self.conn.commit()
        self.close_conn()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def verify_user_credentials(self, username, password): # método para verificar usuário e senha

        self.open_conn() # chama o método de conexao com o banco de dados

        query = "SELECT username, password FROM tab_admins WHERE username = ? AND password = ?" # string de query

        self.cursor.execute(query, (username, password)) # executa a query na tupla

        result = self.cursor.fetchone() # obtém resultado da próxima linha do comando SQL

        self.close_conn() # chama o método para encerrar a conexao

        # Retorna True se o resultado não for None (ou seja, se um usuário foi encontrado),
        # e False caso contrário (nenhum usuário correspondente)
        return result is not None

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    def view_rows(table_name): # método para verificar o conteudo das tabelas

        conn = sqlite3.connect('DB000') # cria um conexao com o sqlite3
        cursor = conn.cursor()          
        
        query = f"SELECT * FROM {table_name};" # string de conexao que recebe um argumento
        
        cursor.execute(query) # executa a query 
        
        rows = cursor.fetchall() # recupera todas as linhas
        
        conn.close() # chama o método para encerrar a conexao
        
        return rows # retorna as linhas da tabela

    # Substitua 'tab_admins' pelo nome da tabela que deseja consultar
    table_name = 'tab_employees'
    result = view_rows(table_name)

    # Exibe o resultado
    print(f"Conteúdo da tabela {table_name}:")
    for row in result:
        print(row)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def fetch_column_names(table_name):

        conn = sqlite3.connect('DB000') # cria um conexao com o sqlite3
        cursor = conn.cursor()
        
        query = f"PRAGMA table_info({table_name});" # string de conexao que recebe um argumento
        
        cursor.execute(query) # Executa a consulta
        
        rows = cursor.fetchall() # Recupera todas as linhas (cada linha contém informações sobre uma coluna) 

        conn.close() # chama o método para encerrar a conexao
        
        column_names = [row[1] for row in rows] # Extrai os nomes das colunas da primeira posição de cada tupla
        
        return column_names # retorna os nomes das colunas

        # Substitua 'tab_admins' pelo nome da tabela que deseja consultar
        table_name = 'tab_employees'
        columns = fetch_column_names(table_name)

        # Exibe o resultado
        print(f"Colunas da tabela {table_name}: {columns}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def drop_table(self, table_name): # metodo para deletar uma tabela

        self.open_conn()
        
        query = f"DROP TABLE IF EXISTS {table_name};"
        self.cursor.execute(query)

        self.conn.commit()
        self.close_conn()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def delete_table(self, table_name): # metodo para deletar o conteudo de uma tabela

        self.open_conn()
        
        query = f"DELETE FROM {table_name};"
        self.cursor.execute(query)

        self.conn.commit()
        self.close_conn()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
