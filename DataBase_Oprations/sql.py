
import mysql.connector as connection
import os
import logging 
class Play_with_Database:

    logging_str = "[%(asctime)s:  %(levelname)s : %(module)s] %(message)s"
    log_dir = 'sql_logs'
    os.makedirs(log_dir,exist_ok=True)
    logging.basicConfig(filename=os.path.join(log_dir,'sql_logs.log'),level=logging.DEBUG, format=logging_str)

    def __init__(self,host ='localhost',user = 'root',password = None):
        self.host = host
        self.user = user
        self.passwd = password
        self.make_connection()
    
    def make_connection(self):
        try:
            logging.info('----------'*10)
            logging.info('making connection >>>>>......')
            
            mydb = connection.connect(host = self.host,
                                  user = self.user,
                                  passwd = self.passwd,
                                  use_pure=True)
            print("Connection is stablished...",mydb)
            logging.info("<<<<<<<<<< Connection is stablished...")
            logging.info("-----"*11)
            return mydb
            
        except Exception as e:
            print('Connection is not stablished . ...',str(e))
            logging.error("Connection is not stablished . ...".format(e))
            
    def creating_database(self,db_name = None):
        try:
            logging.info('----------'*10)
            logging.info('Starte making_connection............')
            mydb = connection.connect(host = self.host,
                                  user = self.user,
                                  passwd = self.passwd,
                                  use_pure=True)
            logging.info('making_connection is done............')
            mycursor = mydb.cursor()
            logging.info('making_cursor is done............')
            logging.info('---'*10)
            logging.info('creating database............')   
            mycursor.execute("CREATE DATABASE {}".format(db_name))
            
            logging.info("Database is created...".format(db_name))
            logging.info('---'*10)
            logging.info(" ")
        except Exception as e:
            
            logging.error("Database is not created...".format(e))

    def check_database(self):
        try:
            logging.info('----------'*10)
            logging.info('Starte making_connection............')
            mydb = connection.connect(host = self.host, 
                                    user = self.user,
                                    passwd = self.passwd,
                                    use_pure=True)
            logging.info('making_connection is done............')
            mycursor=mydb.cursor()
            mycursor.execute("SHOW DATABASES")
            for x in mycursor:
                logging.info(x)
            logging.info("all the database are listed...")
            logging.info('---'*10)
        except Exception as e:
            logging.info('Database is not created . ...',str(e))

    def delete_database(self,db_name = None):
        try:
            logging.info('----------'*10)
            logging.info('Starte making_connection............')
            mydb = connection.connect(host = self.host, 
                                    user = self.user,
                                    passwd = self.passwd,
                                    use_pure=True)
            logging.info('making_connection is done............')
            mycursor=mydb.cursor()
            mycursor.execute("DROP DATABASE {}".format(db_name))
            logging.info(f"Database is deleted...{db_name}")
            logging.info('------'*10)
        except Exception as e:
            logging.exception(f'Database is not deleted . ...{e}')

    def delete_all_database(self):
        logging.info('----------'*10)
        logging.info('Starte making_connection............')
        try:
            mydb = connection.connect(host = self.host, 
                                    user = self.user,
                                    passwd = self.passwd,
                                    use_pure=True)
            logging.info('making_connection is done............')
            mycursor=mydb.cursor()
            mycursor.execute("SHOW DATABASES")
            all_db=[]
            for x in mycursor:
                all_db.append(x[0])
                print(all_db)
            logging.info("----"*10)
            for db in all_db:
                mycursor.execute("DROP DATABASE IF EXISTS {}".format(db))
                
                logging.info(f"Database is deleted...{db}")
            logging.info('------'*10)
                
            logging.info("all the database are deleted...")
            logging.info('---'*10)
        except Exception as e:
            logging.exception(f'Database is not deleted . ...{e}')
    



           
            
            
Play_with_Database(password="123456789").check_database()
