import os 
import mysql.connector as connection
import logging 

logging_str = "[%(asctime)s:  %(levelname)s : %(module)s] %(message)s"
log_dir = 'sql_Table_logs'
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(filename = os.path.join(log_dir,'sql_logs.log'),filemode ='a',level=logging.DEBUG, format=logging_str)

class Play_with_Tables:
    def __init__(self,host ='localhost',user = 'root',password = None,db_name =None):
        self.host = host
        self.user = user
        self.passwd = password
        self.db_name = db_name
    def make_connection(self):
        mydb = connection.connect(host = self.host,
                                  user = self.user, 
                                  passwd = self.passwd,
                                  database= self.db_name,
                                  use_pure=True) 
        logging.info("Connection is stablished...")   
        return mydb
    def create_table(self,table_name = None,columns = None):
        try:
            mydb = self.make_connection()
            mycursor = mydb.cursor()
            logging.info('creating table............')
            mycursor.execute("CREATE TABLE {} ({})".format(table_name,columns))
            logging.info("Table is created...")
            mydb.close()
        except Exception as e:
            logging.error(f"Table is not created...{e}")  

    def insert_data(self,table_name = None,columns = None,values = None):
        try:
            mydb = self.make_connection()
            mycursor = mydb.cursor()
            logging.info('inserting data............')
            mycursor.execute("INSERT INTO {} ({}) VALUES ({})".format(table_name,columns,values))
            logging.info("Data is inserted...")
            mydb.commit()
            mydb.close()
        except Exception as e:
            logging.error(f"Data is not inserted...{e}")
    def check_table(self,table_name = None):
        try:
            logging.info('---'*15)
            logging.info('checking table............')
            mydb = self.make_connection()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM {}".format(table_name))

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)
                logging.info(f"Table is checked...\n {x}")
        except Exception as e:
            logging.error(f"Table is not checked...{e}")


#Play_with_Tables(password='123456789',db_name='ne11').create_table(table_name='users',columns='id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),email VARCHAR(255),password VARCHAR(255)')
Play_with_Tables(password='123456789',db_name='ne11').insert_data(table_name='users',columns='id,name,email,password',values="3,'dipeasndra','dipendra@gmail.com','123456789'")
Play_with_Tables(password='123456789',db_name='ne11').check_table(table_name='users')
