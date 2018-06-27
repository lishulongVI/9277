import pymysql.cursors
conf = dict(
    host='sql-ppingtai01br.cdmdc6lauvsz.sa-east-1.rds.amazonaws.com',
    user='lishulong',
    password='EdTVwfGp8swTvtg8vLvuAidtTeujVD',
    db='wecash_america',
    charset='utf8mb4'
)
def getConnect():
    # Connect to the database
    print('打开链接....')
    return pymysql.connect(
        host=conf['host'],
        user=conf['user'],
        password=conf['password'],
        db=conf['db'],
        charset=conf['charset'],
        cursorclass=pymysql.cursors.DictCursor
    )
class MySqlTemplate(object):
    
    @staticmethod
    def sqlManyExec(sql:str):
        """
        查询列表 为了避免 连接忘记关闭，每次执行都 创建链接 执行完毕 关闭链接
        """
        try:
            connection = getConnect()
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            print('关闭链接....')
            connection.close()
    @staticmethod
    def sqlOneExec(sql:str):
        try:
            connection = getConnect()
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            print('关闭链接....')
            connection.close()