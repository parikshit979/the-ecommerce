import MySQLdb
from time import sleep


class DBConnector(object):
    def __init__(self, host, username, password, port=3306, database=None):
        self.host = host
        self.port = port
        self.user = username
        self.passwd = password
        self.database = database
        self.db = self.get_connection()
        print('Creating DBConnector instance...')

    def __del__(self):
        self.db.close()

    def get_connection(self):
        for i in range(0, 5):
            try:
                db = MySQLdb.connect(host=self.host, port=self.port, user=self.user,
                                     passwd=self.passwd)
                return db
            except MySQLdb.Error, e:
                print str(e)
                print 'Unable to connect to the database. Retrying.... {0}'.format(i + 1)
                sleep(2)
        print "Failed to establish connection after 5 attempts."
        raise MySQLdb.Error

    def execute_single(self, query):
        for i in range(0, 3):
            try:
                self.db.autocommit(False)
                cursor = self.db.cursor()
                cursor.execute(query)
                cursor.close()
                self.db.commit()
                self.db.autocommit(True)
                return True
            except MySQLdb.Error, e:
                print str(e)
                print query
                if str(e).__contains__('2006'):
                    print "Retrying....."
                    self.db = self.get_connection()
                else:
                    print 'Failed execute_single..... Rolling Back'
                    self.db.rollback()
                    self.db.autocommit(True)
                    raise ValueError(str(e.args))
        return False

    def execute_list(self, query_list):
        try:
            self.db.autocommit(False)
            for query in query_list:
                cursor = self.db.cursor()
                print query
                cursor.execute(query)
                cursor.close()
                self.db.commit()
            self.db.autocommit(True)
            return True
        except MySQLdb.Error, e:
            print str(e)
            if str(e).__contains__('2006'):
                print "Retrying....."
                self.db = self.get_connection()
            else:
                print 'Failed execute_single..... Rolling Back'
                self.db.rollback()
                self.db.autocommit(True)
                raise ValueError(str(e.args))
        return False

    def select_query_list(self, query):
        for i in range(0, 3):
            try:
                cursor = self.db.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                data = []
                if cursor.rowcount > 0:
                    for record in result:
                        data.append(record)
                cursor.close()
                return data
            except MySQLdb.Error, e:
                print str(e)
                print query
                if str(e).__contains__('2006'):
                    print "Retrying....."
                    self.db = self.get_connection()
                else:
                    raise ValueError(str(e.args))
        return []

    def select_query_dict(self, query):
        for i in range(0, 3):
            try:
                cursor = self.db.cursor()
                cursor.execute(query)
                data = []
                if cursor.rowcount > 0:
                    columns = [col[0] for col in cursor.description]
                    data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                cursor.close()
                return data
            except MySQLdb.Error, e:
                print str(e)
                print query
                if str(e).__contains__('2006'):
                    print "Retrying....."
                    self.db = self.get_connection()
                else:
                    raise ValueError(str(e.args))
        return []

    def select_query_tuple(self, query):
        for i in range(0, 3):
            try:
                cursor = self.db.cursor()
                cursor.execute(query)
                res = cursor.fetchall()
                cursor.close()
                return res
            except MySQLdb.Error, e:
                print str(e)
                print query
                if str(e).__contains__('2006'):
                    print "Retrying....."
                    self.db = self.get_connection()
                else:
                    raise ValueError(str(e.args))
        return ()
