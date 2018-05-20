import pymysql

from 通讯录Mysql.people import people


class Peopledao:
    def __init__(self):
        pass

    #查询所有联系人信息
    def findall(self):
        conn = self.myconnect()
        cursor = conn.cursor()
        cursor.execute("select * from peoplelist limit 10")
        ret = cursor.fetchall()
        # print(ret)
        conn.close()
        return ret
    #添加联系人信息
    def addpeople(self,p):
        conn = self.myconnect()
        cursor = conn.cursor()
        cursor.execute("insert into peoplelist(name,tel) values('%s',%s)" % (p.name , p.tel))
        conn.commit()
        conn.close()

    #根据姓名修改联系人电话号码
    def myupdate(self,p):
        conn = self.myconnect()
        cursor = conn.cursor()
        cursor.execute("update peoplelist set tel='%s' where name='%s'" % (p.tel,p.name))
        conn.commit()
        conn.close()

    #根据姓名查询信息
    def find(self,name):
        conn = self.myconnect()
        cursor = conn.cursor()
        cursor.execute("select * from peoplelist where name='%s'"%(name))
        ret = cursor.fetchall()
        # print(ret)
        conn.close()
        return ret

    #根据姓名删除联系人
    def mydelete(self,p):
        conn = self.myconnect()
        cursor = conn.cursor()
        cursor.execute("delete from peoplelist where name='%s'" % (p.name))
        conn.commit()
        conn.close()


    def myconnect(self):
        conn = pymysql.connect(
            # 主机和端口
            host="127.0.0.1", port=3306,
            # 用户名和密码
            user="root", password="pzl123456",
            # 数据库和字符集
            database="contact", charset='utf8'
        )
        return conn


dao=Peopledao()
# dao.findall()
# p.addpeople("吴磊","15678922314")
# dao.myupdate("534533354353","吴磊")
# p=people("吴磊","15678922314")
# dao.addpeople(p)

# p=people("吴磊","15789762413")
# dao.myupdate(p)

# p=people("吴磊","15789762413")
# dao.mydelete(p)

# print(dao.find("彭志浪"))

