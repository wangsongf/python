import MySQLdb

class Mysql(object):
    
    def __init__(self):
        self.connect()
    
    def connect(self):

        try:
            self.conn = MySQLdb.connect(
                host = '127.0.0.1',
                user = 'root',
                passwd = '********',
                db = 'test',
                port = 3306,
                charset = 'utf8'
            )
            
        except MySQLdb.Error as e:
            print('Error:%s' % e)

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error:%s' % e)     
        
    def get_a(self):
   
        sql = 'select * from `tdb_goods` where `cate_id` = %s;' 
        cursor = self.conn.cursor()
        cursor.execute(sql,('1',))
        data = cursor.fetchone()
        print(data)
        cursor.close()
        self.close_conn()
    
    def add_a(self):
        sql = "insert into `tdb_goods`(`goods_name`,`cate_id`,`brand_id`,`goods_price`,`is_show`,`is_saleoff`) value (%s,%s,%s,%s,%s,%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql,('伟哥牌notebook','8','1','66666','1','0'))
        cursor.close()
        self.close_conn()
        
def main():
    object = Mysql()
    object.add_a()
    
if __name__ == '__main__':
    main()