import sqlite3
class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
        id Integer primary key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,? )",
                         (name,age,doj,email,gender,contact,address))
        self.con.commit()
    def fetch(self):
     self.cur.execute("SELECT *from employess")
     rows=self.cur.fetchall()
     #print(rows)
        return rows
    #delete a record
    def remove(self,id)
        self.cur.execute("delete  from employees where id=?",(id,))
        self.con.commit()
        #update
        def update(self,name,age,doj,email,gender,contact,address):
            self.cur.execute("update  employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=?"
                         (name,age,doj,email,gender,contact,address))
o = Database("Employee.db")
o.insert("Sam", "25", "12-11-2020", "giritharan900@gmail.com", "Male", "9789176702", "cheery road,salem")

        self.con.commit()



