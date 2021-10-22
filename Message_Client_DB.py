import sqlite3
from datetime import datetime
import logging

#intiallize logging format
FORMAT = "%(filename)s: in line %(lineno)d\n%(message)s"
logging.basicConfig(filename='Debug.log', filemode= "w", level=logging.DEBUG
                    , format= FORMAT)

#class for implementing the data base
class MessageUDB:
    def __init__(self):
        """
        object intiallizer
        creates the tables if not already created
        """
        self.conn = sqlite3.connect('server.db')
        self.conn.text_factory = bytes
        try:

            self.conn.execute('''CREATE TABLE clients
                                 (ID TEXT PRIMARY KEY     NOT NULL,
                                 name          TEXT    NOT NULL,
                                 public_key           TEXT     NOT NULL,
                                 LastSeen TEXT);''')

            self.conn.execute('''CREATE TABLE messages
                                 (ID TEXT PRIMARY KEY     NOT NULL,
                                 ToClient  TEXT        TEXT    NOT NULL,
                                 FromClient TEXT    NOT NULL,
                                 Type char(1),
                                 Content Blob);''')
        except:
            logging.warning("Tables were already created")
            pass
            #Handle the situation of already existing table


    def InsertMessage(self, ID, IDTO, IDFROM, Type, Content ):
        """
        Inserting new Message into data base

        raises an error if error detected
        """

        #intiallizing the current date as Last Seen
        LastSeen = datetime.today().strftime("")

        try:
            #exectuting Insert
            self.conn.execute("""Insert Into messages Values
            (?,?,?,?,?)
            """, [ID, IDTO, IDFROM, Type, Content])
        except:
            #handeling error situation
            raise

    def InsertClient(self, ID, Name, PublicKey):
        """
        Inserting new Client into data base
        inserting the current date as Last seen

        raises an error if clone ID detected
        """

        # intiallizing the current date as Last Seen
        LastSeen = datetime.today().strftime("")

        try:
            # exectuting Insert
            self.conn.execute("""Insert Into clients Values
            (?,?,?,?)
            """, [ID, Name, PublicKey, LastSeen])
        except:
            # handeling clone situation
            logging.error("ID already exists")
            raise


    def Exists(self, attr, value):
        cur = self.conn.cursor()
        try:
            querry = f"SELECT {attr} From clients"
            cur.execute(querry)
            return value in cur.fetchall()
        except:
            logging.debug("wrong attribute")
            return False

    def DeleteMessage(self, ID):
        self.conn.execute("Delete From messages Where Id = ?",[ID])



