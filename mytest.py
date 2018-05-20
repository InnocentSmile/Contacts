from foxyball0_3.foxyball import *

class people1:
    def __init__(self,name=None,tel=None,id=None):
        self.name=name
        self.tel=tel
        self.id=id

if __name__ == '__main__':
    # mapper1=[["peoplelist","people1"],["name","name"],["tel","tel"],["id","id"]]
    cfg=Configuration()
    cfg.addMapper("peoplelist","people1")
    cfg.addRelation("peoplelist","name","name")
    cfg.addRelation("peoplelist", "tel", "tel")
    cfg.addRelation("peoplelist", "id", "id")
    db=ORM(password="pzl123456",database="contact",ormList=cfg.ormList)
    #增
    # p1=people1(name="剑侠客",tel="123")
    # db.insert(p1)
    list=db.queryBySql(people1,"select * from peoplelist where id=40")

    pass
    # #修改（修改的对象必须有id值）
    # p2=db.query(p1)[0]
    # p2.tel="123"
    # db.update(p2)


    # for t in list:
    #     print(t.__dict__)


    # list=[0,1]
    # print(list[4])


