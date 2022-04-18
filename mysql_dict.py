"""
练习： 将单词本存入数据库
    1.创建数据库dict(htf8)
        create database Heat;
    2.创建数据表 HEAT 将heat和具体炉次信息分别存入不同的字段
        create table HEAT(heatnum char(8) primary key not null,钢种 char(6) not null,工序 varchar(4),LF工位 char(2),T varchar(3),钢水量 decimal(4,1) default 0.0);
    3.编写程序将heat存入HEAT表
"""
import  pymysql
f = open('dict.txt',encoding='utf-8')

#连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='lime-3526',database='heat')

#获取游标，用来操作数据库，执行sql语句
cur = db.cursor()


sql = "insert into HEAT (heatnum,钢种,工序,LF工位,T,钢水量) values (%s,%s,%s,%s,%s,%s)"
for line in f:
    if not line:
        break
    data = line
    tmp = data.split('\t')
    heatnum = tmp[0]
    grade = tmp[1]
    process = tmp[3]
    LF_station = tmp[5]
    temp = tmp[7]
    weight = tmp[-1]
    try:
        cur.execute(sql,[heatnum,grade,process,LF_station,temp,weight])
        db.commit()
    except:
        db.rollback()

f.close()
#关闭游标、数据库
cur.close()#游标失效
db.close()#数据库断开连接


