import sqlite3
import configparser


class BaseRepository():

    def __init__(self):
        _config = configparser.ConfigParser()
        _config.read('config.ini', encoding='utf-8')

        print(_config.get('database', 'dbname'))
        try:
            self.conn = sqlite3.connect(_config.get('database', 'dbname'))
        except Exception as ex:
            print(ex)

    def getConn(self):
        return self.conn

    def close(self):
        if self.conn:
            try:
                self.conn.commit()
            except Exception as ex:
                print(ex)
            finally:
                self.conn.close()
